from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("get-book/", views.get_book, name="get_book"),
    path("", views.show_books, name="show_books"),
]
