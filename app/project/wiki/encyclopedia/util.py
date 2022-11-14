#!/usr/bin/env python3

import markdown2
import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from icecream import ic

# verbose icecream
ic.configureOutput(includeContext=True)


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """

    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """

    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """

    acro_list = ["html", "css"]
    if title in acro_list:
        title = title.upper()
    else:
        title = title.capitalize()

    filepath = f"app/project/wiki/entries/{title}.md"

    # TODO: raise 404 page
    try:
        f = default_storage.open(filepath)
        content = markdown2.markdown(f.read().decode("utf-8"))
        return content
    except FileNotFoundError:
        return None
