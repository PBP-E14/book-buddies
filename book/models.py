from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    year_publication = models.IntegerField()
    image_cover = models.CharField(max_length=2000)


class RequestBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    year_publication = models.IntegerField()
    image_cover = models.CharField(max_length=2000)
    is_accepted = models.BooleanField(default=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
