from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.


def show_books(request):
    data = Book.objects.all()

    context = {"books": data}

    return render(request, "show_books.html", context)


def get_book(request):
    data = Book.objects.all()
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
