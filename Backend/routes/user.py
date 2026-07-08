from fastapi import APIRouter
from database.connection import get_connection
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


class User(BaseModel):
    username: str
    password: str


@router.get("/")
def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return [dict(user) for user in users]


@router.post("/")
def create_user(user: User):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (username, password)
        VALUES (?, ?)
        """,
        (user.username, user.password)
    )

    conn.commit()
    conn.close()

    return {"message": "User created"}


@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET username = ?, password = ?
        WHERE id = ?
        """,
        (user.username, user.password, user_id)
    )

    conn.commit()
    conn.close()

    return {"message": "User updated"}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "User deleted"}