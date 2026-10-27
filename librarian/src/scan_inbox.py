from pathlib import Path
import hashlib
import sqlite3

ROOT = Path(r"D:\Knowledge_Librarian")
INBOX = ROOT / "00_INBOX"
DATABASE = ROOT / "catalog" / "database" / "librarian.db"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


known_hashes = {}

connection = sqlite3.connect(DATABASE)
for item in INBOX.iterdir():
    print(f"Path: {item}")
    print(f"Name: {item.name}")
    print(f"Extension: {item.suffix}")
    print(f"Is file: {item.is_file()}")
    print(f"Size: {item.stat().st_size} bytes")
 

    if item.is_file():
        file_hash = calculate_hash(item)
        previous = connection.execute(
            "SELECT sha256 FROM file_locations WHERE file_path = ?",
            (str(item),)
        ).fetchone()
        if previous is None:
            print("STATUS: NEW")
        elif previous[0] == file_hash:
            print("STATUS: UNCHANGED")
        else:
            print("STATUS: MODIFIED")
        connection.execute("""
        INSERT INTO file_locations (file_path, sha256)
        VALUES (?, ?)
        ON CONFLICT(file_path)
        DO UPDATE SET sha256 = excluded.sha256
        """, (str(item), file_hash))
        print(f"SHA-256: {file_hash}")

        if file_hash in known_hashes:
            print(f"DUPLICATE: Matches {known_hashes[file_hash]}")
        else:
            known_hashes[file_hash] = item.name
            print("UNIQUE CONTENT: Hash added to scan dictionary")


    print()

connection.commit()
connection.close()

print("----- SCAN SUMMARY -----")
print(f"Total unique files: {len(known_hashes)}")

