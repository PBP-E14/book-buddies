from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.show_books, name="show_books"),
    path("get-book/", views.get_book, name="get_book"),
    path("get-read-book/", views.get_read_book, name="get_read_book"),
    path("read-book/<int:id>/", views.read_book, name="read_books"),
]
