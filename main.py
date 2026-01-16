import app.List_notes
import app.New_Note
import app.Del_note

# ANSI color codes
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_CYAN = "\033[96m"
COLOR_MAGENTA = "\033[95m"

def main():
    print(f"{COLOR_CYAN}Welcome to NoteApp! 🌟{COLOR_RESET}")
    print(f"{COLOR_YELLOW}Commands:")
    print("  /list   - List all notes")
    print("  /new    - Create a new note")
    print("  /delete    - Delete a  note")
    print("  /exit   - Quit the app" + COLOR_RESET)

    while True:
        choice = input(f"{COLOR_MAGENTA}\nEnter command: {COLOR_RESET}").strip().lower()

        if choice == "/exit":
            print(f"{COLOR_GREEN}Goodbye! 👋{COLOR_RESET}")
            break

        elif choice == "/list":
            app.List_notes.list_note()

        elif choice == "/new":
            app.New_Note.save_note()

        elif choice == "/delete":
            app.Del_note.delete_note()

        else:
            print(f"{COLOR_RED}Unknown command! Please use /list, /new, or /exit.{COLOR_RESET}")


if __name__ == "__main__":
    main()
