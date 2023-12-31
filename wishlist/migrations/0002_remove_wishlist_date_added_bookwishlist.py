# Generated by Django 4.2.6 on 2023-10-27 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0002_auto_20231028_1043"),
        ("wishlist", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wishlist",
            name="date_added",
        ),
        migrations.CreateModel(
            name="BookWishlist",
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
                ("date_added", models.DateField(auto_now_add=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="book.book"
                    ),
                ),
                (
                    "wishlist_panel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wishlist.wishlist",
                    ),
                ),
            ],
        ),
    ]
