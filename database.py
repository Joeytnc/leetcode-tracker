import sqlite3
from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Directory used to store the SQLite database
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Full path to the SQLite database file
DB_PATH = DATA_DIR / "problems.db"


def get_connection():
    """Return a connection to the SQLite database."""

    return sqlite3.connect(DB_PATH)


def initialize_database():
    """Create the SQLite database and tables if they do not exist."""

    conn = get_connection()
    cursor = conn.cursor()

    # Create the problems table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            topic TEXT NOT NULL,
            solved INTEGER NOT NULL,
            review_count INTEGER DEFAULT 0,
            last_reviewed TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("Database initialized")


if __name__ == "__main__":
    initialize_database()