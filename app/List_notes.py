from . import ID_Gen

COLOR_RESET = "\033[0m"
COLOR_CYAN = "\033[96m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"

def list_note():
    data = ID_Gen.load_json()

    if not data:
        print(f"{COLOR_RED}You don't have any notes!{COLOR_RESET}")
        return

    sorted_notes = sorted(data, key=lambda note: note["id"])

    print(f"{COLOR_YELLOW}\n--- Your Notes ---{COLOR_RESET}")
    for note in sorted_notes:
        preview = note["content"][:30] + ("..." if len(note["content"]) > 30 else "")
        print(f"{COLOR_CYAN}ID_{note['id']}{COLOR_RESET} | {COLOR_GREEN}{note['title']}{COLOR_RESET} | {COLOR_YELLOW}{preview}{COLOR_RESET}")
    print(f"{COLOR_YELLOW}-----------------{COLOR_RESET}\n")
