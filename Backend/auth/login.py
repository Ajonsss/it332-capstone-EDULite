from database.connection import get_connection
from Backend.utils.password_hasher import (
    hash_password,
    verify_password
)

def register_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)

    try:
        cursor.execute(
            """
            INSERT INTO users(username, password)
            VALUES (?, ?)
            """,
            (username, hashed)
        )

        conn.commit()
        return True

    except Exception as e:
        print("Database error:", e)
        return False

    finally:
        conn.close()


def login_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:

        stored_password = result[0]

        if verify_password(
            password,
            stored_password
        ):
            return True

    return False