#!/usr/bin/env python3

from . import util
from django.shortcuts import render


def index(request):
    return render(
        request,
        "encyclopedia/index.html",
        {"entries": util.list_entries()}
    )


def entry(request, title):
    return render(
        request,
        "encyclopedia/entry.html",
        {"title": title, "content": util.get_entry(title)},
    )
