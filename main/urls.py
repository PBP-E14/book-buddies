from django.urls import path
from main.views import user_logout, homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('logout/', user_logout, name='logout'),
]