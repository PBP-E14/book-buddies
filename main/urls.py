from django.urls import path
from . import views
from main.views import user_logout

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('logout/', user_logout, name='logout'),
]