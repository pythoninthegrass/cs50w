import random
from . import util
from .forms import MarkdownForm, MarkdownEditForm
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.urls import reverse
from markdownify import markdownify as md
from pathlib import Path

filepath = Path(f"{default_storage.location}/encyclopedia/templates")


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


def get_entries(request):
    query = request.GET["q"]

    try:
        entries, urls = util.search_entries(query)
        return entry(request, query)
    except TypeError:
        # raw list of entries/urls
        entries, urls = util.list_entries()

        # look for partial match in entries
        entries = [entry for entry in entries if query.lower() in entry.lower()]

        # TODO: dynamic `search.html` based on `entries` length (javascript?)
        return render(
            request,
            f"{filepath}/search.html",
            {"query": query, "entries": entries, "urls": urls}
        )


def create(request):
    if request.method == "POST":
        form = MarkdownForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = f"# {title}\n\n" + form.cleaned_data["body"]

            util.save_entry(
                title, body
            )
            return redirect(
                reverse(
                    "entry",
                    args=(form.cleaned_data["title"],)
                )
            )
    else:
        form = MarkdownForm()

    return render(
        request,
        f"{filepath}/create.html",
        {"form": form}
    )


def edit(request, title):
    if request.method == "POST":
        form = MarkdownEditForm(request.POST)
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
        form = MarkdownEditForm()
        form.fields["title"].initial = title
        raw = form.fields["body"].initial = util.get_entry(title)
        form.fields["body"].initial = md(raw)

    return render(
        request,
        f"{filepath}/edit.html",
        {"form": form}
    )


def edit_list(request):
    entries, urls = util.list_entries()

    return render(
        request,
        f"{filepath}/edit_list.html",
        {"entries": entries}
    )


def error404(request, exception):
    return render(
        request,
        f"{filepath}/404.html",
        status=404
    )
