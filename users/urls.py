from django.urls import path
from users.views import user_login, user_profile, register, update_profile, delete_book, filter_books

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('filter_books/', filter_books, name='filter_books'),
]