from django.forms import ModelForm
from forum.models import Forum

class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ["title", "content"]