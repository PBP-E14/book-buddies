from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
]