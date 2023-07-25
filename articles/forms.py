from django import forms
from tinymce.widgets import TinyMCE
from articles.models import Article


class ArticleForm(forms.ModelForm):
    """TinyMCE widget"""

    class Meta:
        model = Article
        widgets = {"content": TinyMCE(attrs={"cols": 80, "rows": 30})}
        fields = ["title", "content", "category"]
