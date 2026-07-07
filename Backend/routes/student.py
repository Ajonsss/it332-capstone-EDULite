from fastapi import APIRouter
from database.connection import get_connection
from pydantic import BaseModel

router = APIRouter(
    prefix="/students",
    tags=["Student"]
)


class Student(BaseModel):
    student_name: str
    scores: int


@router.get("/")
def get_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return [dict(student) for student in students]


@router.post("/")
def create_student(student: Student):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students (student_name, scores)
        VALUES (?, ?)
        """,
        (student.student_name, student.scores)
    )

    conn.commit()
    conn.close()

    return {"message": "Student created"}


@router.put("/{student_id}")
def update_student(student_id: int, student: Student):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET student_name = ?, scores = ?
        WHERE id = ?
        """,
        (student.student_name, student.scores, student_id)
    )

    conn.commit()
    conn.close()

    return {"message": "Student updated"}


@router.delete("/{student_id}")
def delete_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Student deleted"}