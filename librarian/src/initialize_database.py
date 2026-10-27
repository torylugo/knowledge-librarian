from pathlib import Path
import sqlite3

ROOT = Path(r"D:\Knowledge_Librarian")
DATABASE = ROOT / "catalog" / "database" / "librarian.db"

connection = sqlite3.connect(DATABASE)

print("Database connection established!")

connection.execute("""
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY,
    filename TEXT NOT NULL,
    sha256 TEXT NOT NULL
)
""")

connection.execute("""
CREATE TABLE IF NOT EXISTS file_locations (
    id INTEGER PRIMARY KEY,
    file_path TEXT NOT NULL UNIQUE,
    sha256 TEXT NOT NULL
)
""")

connection.commit()
connection.close()

print("Database tables initialized successfully!")