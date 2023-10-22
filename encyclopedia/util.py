import random
import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        # default_storage.delete(filename)
        raise Exception("енциклопедична стаття з наданою назвою вже існує")
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
    
def random_page():
       return  random.choice(list_entries())

def search(title):
    all_searched = []
    all_title = list_entries()
    for item in all_title:
        if title.lower() in item.lower():
            all_searched.append(item)
    return all_searched

def save_edit(title, content):
    print(f"save{title}")
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        print(f"delete {title} !!!!!!!!!!!")
        # raise Exception("енциклопедична стаття з наданою назвою вже існує")
    default_storage.save(filename, ContentFile(content))