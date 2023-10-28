from django.db import models
from users.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    review = models.TextField()
    date = models.DateField(auto_now_add=True)