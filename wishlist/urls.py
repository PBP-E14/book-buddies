from django.urls import path
from wishlist.views import show_wishlist, remove_wishlist, get_wishlist, create_ajax, get_wishlist_book, get_wishlist_json, get_json_by_id

app_name = "wishlist"

urlpatterns = [
    path("", show_wishlist, name="show_wishlist"),
    path("remove_wishlist/<int:wishlist_id>/", remove_wishlist, name="remove_wishlist"),
    path("get_wishlist/", get_wishlist, name="get_wishlist"),
    path("create-ajax/<int:book_id>/", create_ajax, name="create-ajax"),
    path("get_wishlist_book/", get_wishlist_book, name="get_wishlist_book"),
    path("get_wishlist_json/", get_wishlist_json, name="get_wishlist_json"),
    path("json/<int:wishlist_id>/", get_json_by_id, name="get_json_by_id"),
]
