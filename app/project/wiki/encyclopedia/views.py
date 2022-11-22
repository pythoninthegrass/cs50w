#!/usr/bin/env python3

from . import util
from django.core.files.storage import default_storage
from django.shortcuts import render
from pathlib import Path

filepath = Path(f"{default_storage.location}/app/project/wiki/encyclopedia/templates")


def index(request):
    entries, urls = util.list_entries()

    return render(
        request,
        f"{filepath}/index.html",
        {"entries": entries,
        "urls": urls}
    )


def entry(request, title):
    return render(
        request,
        f"{filepath}/entry.html",
        {"title": title, "content": util.get_entry(title)},
    )


def error404(request, exception):
    return render(request, f"{filepath}/404.html", status=404)
