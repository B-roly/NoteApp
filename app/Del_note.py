from . import ID_Gen
import os

# ANSI colors
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
RESET   = "\033[0m"

def delete_note():
    data = ID_Gen.load_json()

    if(data == []):
        print(f"{RED}You don't have any notes to delete!")
        return
    print(f"{CYAN}────────────────────────────")
    print(" 🗑️  DELETE A NOTE")
    print("────────────────────────────" + RESET)

    print(f"{YELLOW}➤ Enter the note ID to delete:{RESET}")
    choice = input("  > ")

    if not choice.isdigit():
        print(f"{RED}✖ Error: ID must be a number{RESET}")
        return
    else:
        choice = int(choice)

        for note in data:
            if choice == note["id"]:
                file_path = "Storage/" + note["title"] + ".json"
                os.remove(file_path)

                print(f"{GREEN}✔ Note deleted successfully!{RESET}")
                print(f"{CYAN}  ID: {note['id']}")
                print(f"  Title: {note['title']}{RESET}")
                return
            else:
                print(f"{RED}✖ Error: ID does not exist{RESET}")
                return