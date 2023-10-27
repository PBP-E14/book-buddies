from django.urls import path
from forum.views import show_forums, create_forum, read_forum, reply_forum, back_to_homepage

urlpatterns = [
    path('show_forums/', show_forums, name='show_forums'),
    path('create_forum/', create_forum, name='create_forum'),
    path('read_forum/<int:id>/', read_forum, name='read_forum'),
    path('reply_forum/<int:id>/', reply_forum, name='reply_forum'),
    path('back_to_homepage/', back_to_homepage, name='back_to_homepage')
]