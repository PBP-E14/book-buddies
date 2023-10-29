from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from forum.models import Forum, Reply
from forum.forms import ForumForm, ReplyForm
from django.db.models import Count
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from users.models import User

# Create your views here.
@login_required(login_url='/login')
def show_forums(request):
    forums = Forum.objects.annotate(reply_count=Count('reply'))
    context = {
        'forums' : forums,
    }
    return render(request, "forum_choice.html", context)

@login_required(login_url='/login')
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

def get_forum_json(request, choice):
    if (choice == 1):
        forums = Forum.objects.all()
    elif (choice == 2):
        forums = Forum.objects.filter(total_reply=0)
    elif (choice == 3):
        forums = Forum.objects.filter(total_reply__gt=0)
    elif (choice == 4):
        forums = Forum.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', forums))

@csrf_exempt
def add_forum_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")

        new_forum = Forum(title=title, content=content)
        new_forum.user = request.user
        new_forum.total_reply = 0
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
        edited_forum = Forum.objects.get(pk=id)
        edited_forum.total_reply += 1
        edited_forum.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_user_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize('json', users))

@csrf_exempt
def remove_forum_button(request, id):
    if request.method == 'DELETE':
        forum = Forum.objects.get(pk=id)
        forum.delete()
        return HttpResponse(b"REMOVED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def remove_reply_button(request, id):
    if request.method == 'DELETE':
        reply = Reply.objects.get(pk=id)
        reply.delete()
        return HttpResponse(b"REMOVED", status=201)
    return HttpResponseNotFound()