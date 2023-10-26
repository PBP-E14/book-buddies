# Generated by Django 4.2.6 on 2023-10-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("publisher", models.CharField(max_length=255)),
                ("year_publication", models.IntegerField()),
                ("image_cover", models.CharField(max_length=2000)),
            ],
        ),
    ]
