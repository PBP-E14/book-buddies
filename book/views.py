from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import Book

# Create your views here.


def get_book(request):
    data = Book.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_books(request):
    data = Book.objects.all()

    context = {"books": data}

    return render(request, "show_books.html", context)
