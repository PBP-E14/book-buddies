from django.urls import path
from users.views import fetch_user_data, show_json, update_profile_flutter, user_login, user_profile, register, update_profile, delete_book, filter_books

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('filter_books/', filter_books, name='filter_books'),
    path('json/', show_json, name='show_json'),
    path('fetch_user_data/', fetch_user_data, name='fetch_user_data'),
    path('update_profile_flutter/', update_profile_flutter, name='update_profile_flutter'),
]