# Generated by Django 4.2.1 on 2023-07-20 01:46

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("content", tinymce.models.HTMLField()),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="modified at"),
                ),
                (
                    "view_count",
                    models.PositiveIntegerField(default=0, verbose_name="view count"),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("TECH", "Technical"),
                            ("FOOD", "Foods"),
                            ("MUSIC", "Musics"),
                            ("EMOTIONS", "Emotions"),
                            ("SCIENCE", "Science"),
                            ("ARTS", "Arts"),
                            ("MISC", "Miscellaneous"),
                        ],
                        default="MISC",
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
