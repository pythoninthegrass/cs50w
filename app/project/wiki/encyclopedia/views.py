#!/usr/bin/env python3

from . import util
from django.shortcuts import render


def index(request):
    entries, urls = util.list_entries()

    return render(
        request,
        "encyclopedia/index.html",
        {"entries": entries,
        "urls": urls}
    )


def entry(request, title):
    return render(
        request,
        "encyclopedia/entry.html",
        {"title": title, "content": util.get_entry(title)},
    )


def error404(request, exception):
    return render(request, "encyclopedia/404.html", status=404)
