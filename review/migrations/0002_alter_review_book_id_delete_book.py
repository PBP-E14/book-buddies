# Generated by Django 4.2.6 on 2023-10-27 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0002_auto_20231028_1043"),
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="book_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="book.book",
            ),
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]
