from django.urls import path
from . import views

urlpatterns = [
    path("view-initial/", views.get_book, name="view_inital"),
]
