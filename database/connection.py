import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "edulite.db"

def get_connection():
    return sqlite3.connect(DATABASE_PATH)