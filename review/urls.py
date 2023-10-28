from django.urls import path
from review.views import show_review, create_review

urlpatterns = [
    path('show_review/', show_review, name='show_review'),
    path('create_review', create_review, name='create_review'),
]