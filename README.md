# 📝 NoteApp --- Python CLI Notes Manager

A simple **command-line note-taking application** written in Python.
This project focuses on **backend logic**, data validation, and clean
program structure without relying on a graphical interface.

------------------------------------------------------------------------

## ✨ Features

-   Create notes from the terminal
-   List existing notes (sorted by ID)
-   Delete notes by ID
-   JSON file storage
-   Automatic ID generation
-   Input sanitization
-   Validation of corrupted or invalid JSON files
-   Colored terminal output for better UX

------------------------------------------------------------------------

## 📁 Project Structure

    NoteApp/
    │
    ├── app/
    │   ├── Note.py          # Note model
    │   ├── New_Note.py      # Create new notes
    │   ├── List_notes.py    # List notes
    │   ├── Del_note.py      # Delete notes
    │   ├── ID_Gen.py        # ID generation & data loading
    │
    ├── storage/             # JSON note files (auto-created)
    ├── main.py              # Application entry point

------------------------------------------------------------------------

## ▶️ How to Run

Make sure you have **Python 3.10+** installed.

``` bash
python main.py
```

------------------------------------------------------------------------

## 💬 Available Commands

    /list    → List all saved notes
    /new     → Create a new note
    /delete  → Delete a note by ID
    /exit    → Exit the application

------------------------------------------------------------------------

## 🧠 What This Project Demonstrates

-   Backend-oriented thinking
-   File-based persistence
-   Defensive programming
-   Error handling
-   Modular Python design
-   Clean CLI interaction

This project was built as a **learning and portfolio project**.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Search notes by title
-   Edit existing notes
-   Export notes to a single file
-   Database support (SQLite)
-   REST API version (FastAPI / Flask)
-   Unit tests

------------------------------------------------------------------------

## 📜 License

This project is open-source and free to use for learning purposes.
