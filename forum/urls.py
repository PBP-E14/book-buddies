from django.urls import path
from forum.views import show_forums, read_forum, get_forum_json, add_forum_ajax, \
    get_reply_json, add_reply_ajax, get_user_json, remove_forum_button, remove_reply_button, show_json_forum, \
    show_json_reply, show_json_reply_byId, create_forum_flutter

urlpatterns = [
    path('show_forums/', show_forums, name='show_forums'),
    path('show_forums/read_forum/<int:id>/', read_forum, name='read_forum'),
    path('get_forum_json/<int:choice>/', get_forum_json, name='get_forum_json'),
    path('add_forum_ajax/', add_forum_ajax, name='add_forum_ajax'),
    path('get_reply_json/<int:id>/', get_reply_json, name='get_reply_json'),
    path('add_reply_ajax/<int:id>/', add_reply_ajax, name='add_reply_ajax'),
    path('get_user_json/', get_user_json, name='get_user_json'),
    path('remove_forum_button/<int:id>/', remove_forum_button, name='remove_forum_button'),
    path('remove_reply_button/<int:id>/', remove_reply_button, name='remove_reply_button'),
    path('show_json_forum/', show_json_forum, name='show_json_forum'),
    path('show_json_reply/', show_json_reply, name='show_json_reply'),
    path('show_json_reply_byId/<int:id>/', show_json_reply_byId, name='show_json_reply_byId'),
    path('create-forum-flutter/', create_forum_flutter, name='create_forum_flutter'),
]