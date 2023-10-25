from django.urls import path
from forum.views import show_forums, create_forum

urlpatterns = [
    path('show_forums/', show_forums, name='show_forums'),
    path('create_forums/', show_forums, name='create_forums'),
]