from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from forum.models import Forum, Reply
from forum.forms import ForumForm

# Create your views here.
def show_forums(request):
    forums = Forum.objects.all()
    context = {
        'forums' : forums
    }
    return render(request, "forum_choice.html", context)

def create_forum(request):
    form = ForumForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        forum = form.save(commit=False)
        forum.user = request.user
        forum.save()
        return HttpResponseRedirect(reverse('forum:show_forums'))
    
    context = {
        'form': form,
        }
    return render(request, "create_forum.html", context)

#belum selesai
def read_forum(request, id):
    forum = Forum.objects.get(pk=id)
    replies = Reply.objects.filter(forum_id=id)
    ...

def reply_forum(request, id):
    ...