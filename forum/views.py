import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
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

def show_json_forum(request):
    data = Forum.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_reply(request):
    data = Reply.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_reply_byId(request, id):
    data = Reply.objects.filter(forum_id=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

@csrf_exempt
def create_forum_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Forum.objects.create(
            user = User.objects.get(pk=data["thisUser"]),
            title = data["title"],
            content = data["content"],
            total_reply = 0
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def create_reply_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        forum = Forum.objects.get(pk=data["thisForum"])
        forum.total_reply += 1

        new_product = Reply.objects.create(
            user = User.objects.get(pk=data["thisUser"]),
            content = data["content"],
            forum_id = forum,
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)