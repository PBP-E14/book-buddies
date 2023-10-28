from django.urls import path
from forum.views import show_forums, read_forum, back_to_homepage, get_forum_json, add_forum_ajax, get_reply_json, add_reply_ajax

urlpatterns = [
    path('show_forums/', show_forums, name='show_forums'),
    path('show_forums/read_forum/<int:id>/', read_forum, name='read_forum'),
    path('back_to_homepage/', back_to_homepage, name='back_to_homepage'),
    path('get_forum_json/', get_forum_json, name='get_forum_json'),
    path('add_forum_ajax/', add_forum_ajax, name='add_forum_ajax'),
    path('get_reply_json/<int:id>/', get_reply_json, name='get_reply_json'),
    path('add_reply_ajax/<int:id>/', add_reply_ajax, name='add_reply_ajax'),
]