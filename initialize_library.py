from pathlib import Path

import sys

if len(sys.argv) < 2:
    print("ERROR: A library root directory is required.")
    print(r"Example: python initialize_library.py D:\Knowledge_Librarian")
    sys.exit()
else:
    ROOT = Path(sys.argv[1])


FOLDERS = [
    "00_INBOX",
    "01_LIBRARY",
    "02_NEEDS_REVIEW",
    "03_DUPLICATES",
    "04_QUARANTINE",
    "catalog/database",
    "catalog/metadata",
    "catalog/logs",
    "librarian/src",
    "librarian/config",
    "librarian/tests",
]


def create_library_structure():
    print(f"Initializing Knowledge Librarian at:\n{ROOT}\n")

    if not ROOT.exists():
        print("ERROR: Root folder does not exist.")
        return

    for folder in FOLDERS:
        folder_path = ROOT / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created/verified: {folder_path}")

    print("\nKnowledge Librarian structure initialized successfully.")


if __name__ == "__main__":
    create_library_structure()