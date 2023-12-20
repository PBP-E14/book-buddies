from django.urls import path
from review.views import show_review,add_review_ajax, get_user_json, get_review_id, show_json_review, create_review_flutter

urlpatterns = [
    path('show_review/', show_review, name='show_review'),
    path('create_review_ajax/', add_review_ajax, name='add_review_ajax'),
    path('get_user_json/', get_user_json, name='get_user_json'),
    path('get_review_id/<int:select_option>/', get_review_id, name='get_review_id'),
    path('show_json_review/', show_json_review, name='show_json_review'),
    path('create-flutter/', create_review_flutter, name='create_review_flutter')
]