# Generated by Django 4.2.1 on 2023-07-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="view_count",
            field=models.IntegerField(default=0, verbose_name="view count"),
        ),
    ]
