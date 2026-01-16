from .Note import Note
from . import ID_Gen
import json

COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_CYAN = "\033[96m"
COLOR_MAGENTA = "\033[95m"

file_path = "storage"

def remove_whitespaces(title):
    return title.replace(" ", "_")

def pars_title(title):
    title = remove_whitespaces(title)
    for c in title:
        if c == '_' or c.isalnum():
            continue
        else:
            return None
    return title

def n_note():
    while True:
        print(f"{COLOR_CYAN}Note Title:{COLOR_RESET}")
        title = input()
        print(f"{COLOR_CYAN}Note Content:{COLOR_RESET}")
        content = input()

        if not title or not content:
            print(f"{COLOR_RED}Title or content cannot be empty!{COLOR_RESET}")
            continue
        else:
            note = Note(title, ID_Gen.id_gen(), content)
            return note

def save_note():
    note = n_note()
    file_name = pars_title(note.title)
    if not file_name:
        print(f"{COLOR_RED}Error parsing the note title! Only letters, numbers, and underscores are allowed.{COLOR_RESET}")
    else:
        save_dir = f"{file_path}/{file_name}.json"
        try:
            with open(save_dir, "w") as f:
                json.dump(note.set_json(), f)
            print(f"{COLOR_GREEN}Note '{note.title}' saved successfully! ✅{COLOR_RESET}")
        except Exception as e:
            print(f"{COLOR_RED}Failed to save note: {e}{COLOR_RESET}")
