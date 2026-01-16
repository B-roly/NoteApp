import json
import os

COLOR_RESET = "\033[0m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_GREEN = "\033[92m"

def pars(note):
    if not isinstance(note, dict):
        return False

    valid_keys = ["id", "title", "content"]
    for key in valid_keys:
        if key not in note:
            return False

    if not isinstance(note["id"], int):
        return False
    if not isinstance(note["title"], str):
        return False
    if not isinstance(note["content"], str):
        return False

    return True

def load_json():
    data = []
    if not os.path.exists("storage"):
        print(f"{COLOR_YELLOW}Storage folder does not exist. Creating...{COLOR_RESET}")
        os.makedirs("storage")

    files = os.listdir("storage")
    if not files:
        print(f"{COLOR_YELLOW}No notes found in storage.{COLOR_RESET}")

    for fl in files:
        title, ext = os.path.splitext(fl)
        if ext == ".json":
            path = f"storage/{fl}"
            try:
                with open(path, "r") as f:
                    note = json.load(f)
                    if pars(note):
                        data.append(note)
                    else:
                        print(f"{COLOR_RED}Skipping invalid note in file: {fl}{COLOR_RESET}")
            except json.JSONDecodeError:
                print(f"{COLOR_RED}Skipping invalid JSON file: {fl}{COLOR_RESET}")
            except Exception as e:
                print(f"{COLOR_RED}Error reading file {fl}: {e}{COLOR_RESET}")
        else:
            continue
    return data

def get_id():
    data = load_json()
    if not data:
        return 0
    return max(note["id"] for note in data)

def id_gen():
    last_id = get_id()
    return last_id + 1 if last_id != 0 else 1

