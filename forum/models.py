from django.db import models
from users.models import User

class Forum(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

class Reply(models.Model):
    content = models.TextField()
    forum_id = models.ForeignKey(Forum, on_delete=models.CASCADE)
