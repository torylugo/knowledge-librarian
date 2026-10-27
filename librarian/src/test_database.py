from pathlib import Path
import sqlite3

ROOT = Path(r"D:\Knowledge_Librarian")
DATABASE = ROOT / "catalog" / "database" / "librarian.db"

connection = sqlite3.connect(DATABASE)

cursor = connection.execute(
    "SELECT id, file_path, sha256 FROM file_locations"
)

for record in cursor:
    print(record)

connection.close()