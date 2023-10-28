from django.urls import path
from forum.views import show_forums, read_forum, back_to_homepage, get_forum_json, add_forum_ajax, \
    get_reply_json, add_reply_ajax, get_user_json, remove_forum_button, remove_reply_button

urlpatterns = [
    path('show_forums/', show_forums, name='show_forums'),
    path('show_forums/read_forum/<int:id>/', read_forum, name='read_forum'),
    path('back_to_homepage/', back_to_homepage, name='back_to_homepage'),
    path('get_forum_json/<int:choice>/', get_forum_json, name='get_forum_json'),
    path('add_forum_ajax/', add_forum_ajax, name='add_forum_ajax'),
    path('get_reply_json/<int:id>/', get_reply_json, name='get_reply_json'),
    path('add_reply_ajax/<int:id>/', add_reply_ajax, name='add_reply_ajax'),
    path('get_user_json/', get_user_json, name='get_user_json'),
    path('remove_forum_button/<int:id>/', remove_forum_button, name='remove_forum_button'),
    path('remove_reply_button/<int:id>/', remove_reply_button, name='remove_reply_button'),
]