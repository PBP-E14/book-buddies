# Generated by Django 4.2.6 on 2023-10-29 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_has_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='has_read',
        ),
    ]
