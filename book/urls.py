from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.show_books, name="show_books"),
    path("history/", views.show_request_history, name="show_request_history"),
    path("admin/", views.show_request_admin, name="show_request_admin"),
    path("get-book/", views.get_book, name="get_book"),
    path("get-read-book/", views.get_read_book, name="get_read_book"),
    path("read-book/<int:id>/", views.read_book, name="read_books"),
    path("delete-book/<int:id>/", views.delete_book, name="delete_book"),
    path("request_add_book", views.request_add_book, name="request_add_book"),
    path(
        "get-all-request-book/", views.get_all_request_book, name="get_all_request_book"
    ),
    path("get-request-book/", views.get_request_book, name="get_request_book"),
    path("cancel-request/<int:id>/", views.cancelRequest, name="cancel_request"),
    path("accept-request/<int:id>/", views.acceptRequest, name="accept_request"),
    path("check-superuser/", views.checkSuperUser, name="check_superuser"),
]
