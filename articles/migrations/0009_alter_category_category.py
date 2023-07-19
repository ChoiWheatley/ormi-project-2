# Generated by Django 4.2.1 on 2023-07-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0008_alter_category_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category",
            field=models.CharField(
                choices=[
                    ("테크", "Tech"),
                    ("음식", "Food"),
                    ("감정", "Emotions"),
                    ("기타", "Miscellaneous"),
                ],
                max_length=255,
            ),
        ),
    ]
