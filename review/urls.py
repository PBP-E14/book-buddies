from django.urls import path
from review.views import show_review, create_review, get_review_json, add_review_ajax, get_user

urlpatterns = [
    path('show_review/', show_review, name='show_review'),
    path('create_review', create_review, name='create_review'),
    path('get-review/', get_review_json, name='get_review_json'),
    path('create_review_ajax/', add_review_ajax, name='add_review_ajax'),
    path('get_user/', get_user, name='get_user'),
]