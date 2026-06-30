from connection import get_connection

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT UNIQUE NOT NULL,
            scores TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")