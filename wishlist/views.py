from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.core import serializers
from .models import Wishlist
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from book.models import Book
import json
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="")
def show_wishlist(request):
    # wishlists = Wishlist.objects.filter(user=request.user)
    # book = []
    # for wishlist in wishlists:
    #     book.append(Book.objects.get(pk=wishlist.book.pk))
    # print(book)
    # context = {
    #     'wishlists': wishlists,
    #     'books': book,
    # }

    return render(request, "show_wishlist.html")


@csrf_exempt
def remove_wishlist(request, wishlist_id):
    if request.method == "DELETE":
        wishlist = Wishlist.objects.get(pk=wishlist_id, user=request.user)
        wishlist.delete()
        return HttpResponse(b"REMOVED", status=201)
    return HttpResponseNotFound()


def get_wishlist(request):
    product_wishlist = Wishlist.objects.filter(user=request.user)
    books = [wishlist.book for wishlist in product_wishlist]

    # Serialize the QuerySet to JSON using Django's serializers
    wishlist_data = serializers.serialize("json", product_wishlist)
    book_data = serializers.serialize("json", books)
    data = {"wishlists": wishlist_data, "books": book_data}
    return JsonResponse(data, safe=False)

def get_wishlist_book(request):
    product_wishlist = Wishlist.objects.filter(user=request.user)
    data = []
    for wishlist in product_wishlist:
        wishlist_obj = {
            "pk": wishlist.pk,
            "fields": {
                "book": {
                    "pk": wishlist.book.pk,
                    "title": wishlist.book.title,
                    "author": wishlist.book.author,
                    "publisher": wishlist.book.publisher,
                    "year_publication": wishlist.book.year_publication,
                    "image_cover": wishlist.book.image_cover,
                },
                "user": wishlist.user.username,
            },
        }
        data.append(wishlist_obj)

    return JsonResponse({"result": data})


@csrf_exempt
def create_ajax(request, book_id):
    if request.method == "POST":
        try:
            book = Book.objects.get(pk=book_id)

        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

        wishlist_item = Wishlist(user=request.user, book=book)
        wishlist_item.save()

        return JsonResponse({"message": "Book added to the wishlist"})

    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_wishlist_json(request):
    wishlists = Wishlist.objects.all()
    return HttpResponse(
        serializers.serialize("json", wishlists), content_type="application/json"
    )

def get_json_by_id(request, id):
    wishlists = Wishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', wishlists))
