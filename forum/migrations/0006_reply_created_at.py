# Generated by Django 4.2.5 on 2023-10-26 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_reply_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
