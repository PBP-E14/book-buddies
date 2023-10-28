from django.urls import path
from wishlist.views import show_wishlist, remove_wishlist, get_wishlist_json

app_name='wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('remove_wishlist/<int:wishlist_id>/', remove_wishlist, name='remove_wishlist'),
    path('get-wishlist/', get_wishlist_json, name='get_wishlist_json'),
]