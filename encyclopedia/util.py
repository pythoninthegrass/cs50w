

import markdown2
import re
from django.core.exceptions import ValidationError
# from django.core.files.base import ContentFile
from django.core.files.storage import default_storage, Storage
from django.http import Http404, HttpResponse
from icecream import ic
from pathlib import Path

# verbose icecream
ic.configureOutput(includeContext=True)

filepath = Path(f"{default_storage.location}/encyclopedia/entries")


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """

    _, filenames = default_storage.listdir(filepath)
    files = list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))

    # basename of files
    urls = [Path(filename).stem for filename in files]

    # lower case urls
    urls = [url.lower() for url in urls]

    # TODO: add endpoint 'wiki' to index redirect vs. hardcode
    # convert urls to hyperlinks
    urls = [f"<a href='/wiki/{url}'>{url}</a>" for url in urls]

    return files, urls


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """

    filename = f"{title}.md"
    Path(f"{filepath}/{filename}").write_text(content)


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """

    # TODO: break out into function (e.g., `validate_entry()`)
    acro_list = ["html", "css"]
    if title in acro_list:
        title = title.upper()
    else:
        title = title.capitalize()

    filename = f"{filepath}/{title}.md"

    try:
        f = default_storage.open(filename)
        content = markdown2.markdown(f.read().decode("utf-8"))
        return content
    except FileNotFoundError:
        raise Http404("Page not found.")


def search_entries(query):
    """
    Searches for an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """

    # get list of entries
    entries, urls = list_entries()
    normalized_entries = [entry.lower().strip() for entry in entries]

    try:
        index = normalized_entries.index(query.lower())
        return entries[index], urls[index]
    except ValueError:
        return None
