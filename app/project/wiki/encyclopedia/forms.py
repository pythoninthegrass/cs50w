from django import forms
from .models import *


class MarkdownForm(forms.ModelForm):
    class Meta:
        model = Markdown
        fields = '__all__'
