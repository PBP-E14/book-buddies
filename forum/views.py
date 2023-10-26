from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from forum.models import Forum, Reply
from forum.forms import ForumForm, ReplyForm
from django.db.models import Count

# Create your views here.
def show_forums(request):
    forums = Forum.objects.annotate(reply_count=Count('reply'))
    context = {
        'forums' : forums,
    }
    return render(request, "forum_choice.html", context)

def create_forum(request):
    form = ForumForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        forum = form.save(commit=False)
        forum.user = request.user
        forum.save()
        return HttpResponseRedirect(reverse('show_forums'))
    
    context = {
        'form': form,
        }
    return render(request, "create_forum.html", context)

#belum selesai
def read_forum(request, id):
    forum = Forum.objects.get(pk=id)
    replies = Reply.objects.filter(forum_id=id)
    context = {
        'forum' : forum,
        'replies' : replies,
        'reply_count' : len(replies)
    }
    return render(request, "read_forum.html", context)

def reply_forum(request, id):
    forum = Forum.objects.get(pk=id)
    form = ReplyForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        reply = form.save(commit=False)
        reply.user = request.user
        reply.forum_id = forum
        reply.save()
        return HttpResponseRedirect(reverse('read_forum', kwargs={'id':id}))
    
    context = {
        'forum' : forum,
        'form': form,
        }
    return render(request, "reply_forum.html", context)

def back_to_homepage(request):
    return render(request, "homepage.html")