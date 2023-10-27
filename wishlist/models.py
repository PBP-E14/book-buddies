from django.db import models
from users.models import User
from book.models import Book

# Create your models here.

class Wishlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
