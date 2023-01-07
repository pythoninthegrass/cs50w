import random
from . import util
from .forms import PostForm
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.urls import reverse
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


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            util.save_entry(
                form.cleaned_data["title"], form.cleaned_data["body"]
            )
            return redirect(
                reverse(
                    "entry",
                    args=(form.cleaned_data["title"],)
                )
            )
    else:
        form = PostForm()

    return render(
        request,
        f"{filepath}/create.html",
        {"form": form}
    )


def error404(request, exception):
    return render(
        request,
        f"{filepath}/404.html",
        status=404
    )
