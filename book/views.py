import json
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseNotAllowed,
    JsonResponse,
)
from django.core import serializers
from django.shortcuts import render
from wishlist.models import Wishlist
from .models import Book, RequestBook
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def show_books(request):
    data = Book.objects.all()

    context = {"books": data}

    return render(request, "show_books.html", context)


def show_request_history(request):
    return render(request, "request_history.html")


def show_request_admin(request):
    return render(request, "book_admin.html")


def get_book(request):
    data = Book.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def get_all_request_book(request):
    data = RequestBook.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def get_request_book(request):
    data = RequestBook.objects.filter(user=request.user)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


@login_required(login_url="/user/login")
def get_read_book(request):
    data = request.user.history_books.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


@login_required(login_url="/user/login")
def read_book(request, id):
    book = Book.objects.get(pk=id)
    request.user.history_books.add(book)
    return HttpResponse(status=200)


@login_required(login_url="/user/login")
@csrf_exempt
def delete_book(request, id):
    if request.method == "DELETE" and request.user.is_superuser:
        book = Book.objects.get(pk=id)
        book.delete()
        return HttpResponse(status=200)

    return HttpResponseNotAllowed()


@login_required(login_url="/user/login")
@csrf_exempt
def request_add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publisher = request.POST.get("publisher")
        year_publication = request.POST.get("year")
        image_cover = request.POST.get("image")
        user = request.user

        new_request = RequestBook(
            title=title,
            author=author,
            publisher=publisher,
            year_publication=year_publication,
            image_cover=image_cover,
            user=user,
        )
        new_request.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


@csrf_exempt
def request_add_book_flutter(request):
    if request.method == "POST":
        if request.user:
            data = json.loads(request.body)

            new_product = RequestBook.objects.create(
                title=data["title"],
                author=data["author"],
                publisher=data["publisher"],
                year_publication=int(data["year_publication"]),
                image_cover=data["image_cover"],
                user=request.user,
            )

            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


def acceptRequest(request, id):
    request_book = RequestBook.objects.get(pk=id)
    book = Book(
        title=request_book.title,
        author=request_book.author,
        publisher=request_book.publisher,
        year_publication=request_book.year_publication,
        image_cover=request_book.image_cover,
    )
    book.save()
    request_book.is_accepted = True
    request_book.save()

    return HttpResponse(status=201)


@csrf_exempt
def cancelRequest(request, id):
    if request.method == "DELETE":
        request_book = RequestBook.objects.get(pk=id)
        request_book.delete()
        return HttpResponse(status=200)

    return HttpResponseNotAllowed()


def checkSuperUser(request):
    result = {"is_superuser": request.user.is_superuser}
    return JsonResponse(result)


def get_book_flutter(request):
    all_book = Book.objects.all()
    read_book = request.user.history_books.all()
    product_wishlist = Wishlist.objects.filter(user=request.user)

    serialize_book = serializers.serialize("json", all_book)
    serialize_read_book = serializers.serialize("json", read_book)
    all_book = json.loads(serialize_book)
    read_book = json.loads(serialize_read_book)

    read_book_pk = []
    for read in read_book:
        read_book_pk.append(read["pk"])

    wishlist_book_pk = []
    wishlist_pk_with_book = {}
    for wishlist in product_wishlist:
        wishlist_book_pk.append(wishlist.book.pk)
        wishlist_pk_with_book[wishlist.book.pk] = wishlist.pk

    result_book = []
    for book in all_book:
        book["fields"]["isRead"] = False
        book["fields"]["isWishlist"] = False
        book["fields"]["wishlistPk"] = -1

        if book["pk"] in read_book_pk:
            book["fields"]["isRead"] = True

        if book["pk"] in wishlist_book_pk:
            book["fields"]["isWishlist"] = True
            book["fields"]["wishlistPk"] = wishlist_pk_with_book[book["pk"]]

        result_book.append(book)

    return JsonResponse(result_book, safe=False)
