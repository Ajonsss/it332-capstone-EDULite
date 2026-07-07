import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "edulite.db"

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # allows dictionary-like results
    return conn