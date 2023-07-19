import tinymce.models
from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as lazy


class Article(models.Model):
    """Model of articles"""

    title = models.CharField(max_length=255)

    # rich text editor HTML Field
    content = tinymce.models.HTMLField()

    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)

    modified_at = models.DateTimeField(verbose_name="modified at", auto_now=True)

    # Article }o--|| User
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    view_count = models.PositiveIntegerField(verbose_name="view count", default=0)

    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    class Category(models.TextChoices):
        TECH = "TECH", lazy("기술")
        FOOD = 'FOOD', lazy("음식")
        MUSIC = "MUSIC", lazy("음악")
        EMOTIONS = "EMOTIONS", lazy("감정")
        SCIENCE = "SCIENCE", lazy("과학")
        ARTS = "ARTS", lazy("예술")
        ANNOUNCE = "ANNOUNCE", lazy("공지")
        MISC = "MISC", lazy("기타")

    # Article }o--|| Category
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.MISC)
