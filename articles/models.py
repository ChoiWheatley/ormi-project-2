import tinymce.models
from django.db import models
from users.models import User


class Article(models.Model):
    """Model of articles"""

    title = models.CharField(max_length=255)
    # rich text editor HTML Field
    content = tinymce.models.HTMLField()
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="modified at", auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.IntegerField(verbose_name="view count", default=0)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
