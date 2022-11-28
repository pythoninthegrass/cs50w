#!/usr/bin/env python3

from django.db import models
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class MarkedDownExample(models.Model):
    title = models.CharField(max_length=200)
    markdown_description = MarkdownxField()

    @property
    def formatted_markdown(self):
        return markdownify(self.markdown_description)

    def get_absolute_url(self):
        return reversed('markdown-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
