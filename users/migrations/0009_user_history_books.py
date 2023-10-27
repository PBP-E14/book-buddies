# Generated by Django 4.2.6 on 2023-10-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20231026_0029'),
        ('users', '0008_remove_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='history_books',
            field=models.ManyToManyField(blank=True, related_name='readers', to='book.book'),
        ),
    ]
