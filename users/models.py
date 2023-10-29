from django.contrib.auth.models import AbstractUser
from django.db import models
from book.models import Book

class User(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    bio = models.TextField(blank=True)
    history_books = models.ManyToManyField(Book, related_name='readers', blank=True)