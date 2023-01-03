#!/usr/bin/env python3

from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('title', 'content')
