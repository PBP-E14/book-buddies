from django.urls import path
from wishlist.views import show_wishlist, remove_wishlist, get_wishlist, create_ajax, get_wishlist_book

app_name = "wishlist"

urlpatterns = [
    path("", show_wishlist, name="show_wishlist"),
    path("remove_wishlist/<int:wishlist_id>/", remove_wishlist, name="remove_wishlist"),
    path("get_wishlist/", get_wishlist, name="get_wishlist"),
    path("create-ajax/<int:book_id>/", create_ajax, name="create-ajax"),
    path("get_wishlist_book/", get_wishlist_book, name="get_wishlist_book"),
]
