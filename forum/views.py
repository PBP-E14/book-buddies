from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from forum.models import Forum, Reply
from forum.forms import ForumForm, ReplyForm
from django.db.models import Count
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from users.models import User

# Create your views here.
def show_forums(request):
    forums = Forum.objects.annotate(reply_count=Count('reply'))
    context = {
        'forums' : forums,
    }
    return render(request, "forum_choice.html", context)

def read_forum(request, id):
    forum = Forum.objects.get(pk=id)
    replies = Reply.objects.filter(forum_id=id)
    context = {
        'forum' : forum,
        'replies' : replies,
        'reply_count' : len(replies)
    }
    return render(request, "read_forum.html", context)

def back_to_homepage(request):
    return render(request, "homepage.html")

def get_forum_json(request):
    forums = Forum.objects.annotate(reply_count=Count('reply'))
    return HttpResponse(serializers.serialize('json', forums))

@csrf_exempt
def add_forum_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")

        new_forum = Forum(title=title, content=content)
        new_forum.user = request.user
        new_forum.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_reply_json(request, id):
    replies = Reply.objects.filter(forum_id=id)
    return HttpResponse(serializers.serialize('json', replies))

@csrf_exempt
def add_reply_ajax(request, id):
    if request.method == 'POST':
        content = request.POST.get("content")

        new_reply = Reply(content=content)
        new_reply.forum_id = Forum.objects.get(pk=id)
        new_reply.user = request.user
        new_reply.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()