#!/usr/bin/env python3

from django.db import models
# from django import template
# from datetime import datetime, timedelta
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField()

    def __str__(self):
        return self.title
