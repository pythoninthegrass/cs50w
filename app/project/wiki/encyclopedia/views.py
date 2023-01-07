#!/usr/bin/env python3

import random
from . import util
from .forms import PostForm
from django.core.files.storage import default_storage
from django.shortcuts import render
from pathlib import Path

filepath = Path(f"{default_storage.location}/app/project/wiki/encyclopedia/templates")


def index(request):
    entries, urls = util.list_entries()

    return render(
        request,
        f"{filepath}/index.html",
        {"entries": entries, "urls": urls}
    )


def entry(request, title):
    return render(
        request,
        f"{filepath}/entry.html",
        {"title": title, "content": util.get_entry(title)},
    )


# TODO: store last entry to avoid duplicate rolls until cycle completes
def random_entry(request):
    entries, urls = util.list_entries()

    rng = random.randint(0, len(entries) - 1)
    title = entries[rng]

    return entry(request, title)


# TODO: handle bare except
def get_entries(request):
    query = request.GET["q"]

    try:
        entries, urls = util.search_entries(query)
        return entry(request, query)
    except:
        entries, urls = util.list_entries()
        return render(
            request,
            f"{filepath}/search.html",
            {"query": query, "entries": entries, "urls": urls}
        )

def error404(request, exception):
    return render(
        request,
        f"{filepath}/404.html",
        status=404
    )
