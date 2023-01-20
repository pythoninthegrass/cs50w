from django.db import models
from markdownx.models import MarkdownxField


class Markdown(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField()

    def __str__(self):
        return self.title
