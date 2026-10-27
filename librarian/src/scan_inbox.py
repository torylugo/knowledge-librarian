from pathlib import Path
import hashlib

ROOT = Path(r"D:\Knowledge_Librarian")
INBOX = ROOT / "00_INBOX"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()
known_hashes = {}

for item in INBOX.iterdir():
    print(f"Path: {item}")
    print(f"Name: {item.name}")
    print(f"Extension: {item.suffix}")
    print(f"Is file: {item.is_file()}")
    print(f"Size: {item.stat().st_size} bytes")
 

    if item.is_file():
        file_hash = calculate_hash(item)
        print(f"SHA-256: {file_hash}")

        if file_hash in known_hashes:
            print(f"DUPLICATE: Matches {known_hashes[file_hash]}")
        else:
            known_hashes[file_hash] = item.name
            print("NEW FILE: Hash added to dictionary")


    print()

print("----- SCAN SUMMARY -----")
print(f"Total unique files: {len(known_hashes)}")