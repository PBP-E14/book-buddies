from django.urls import path
from review.views import show_review,add_review_ajax, get_user_json, get_review_id

urlpatterns = [
    path('show_review/', show_review, name='show_review'),
    path('create_review_ajax/', add_review_ajax, name='add_review_ajax'),
    path('get_user_json/', get_user_json, name='get_user_json'),
    path('get_review_id/<int:select_option>/', get_review_id, name='get_review_id')
]