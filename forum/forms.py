from django.forms import ModelForm
from forum.models import Forum, Reply

class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ["title", "content"]

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ["content"]