from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


class FlatPageForm(forms.ModelForm):
    """TinyMCE widget"""

    class Meta:
        model = FlatPage
        widgets = {"content": TinyMCE(attrs={"cols": 80, "rows": 30})}
        fields = []
