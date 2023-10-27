from django.urls import path
from wishlist.views import show_wishlist, remove_item, get_item_json

app_name='wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('remove_item/<int:item_id>/', remove_item, name='remove_item'),
    path('get-item/', get_item_json, name='get_item_json'),
]