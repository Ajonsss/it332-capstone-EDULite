from database.connection import get_connection

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    for row in cursor.fetchall():
        print(row)

    conn.close()


def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Student name: ")
    score = input("Score: ")

    cursor.execute(
        "INSERT INTO students(student_name, scores) VALUES (?, ?)",
        (name, score)
    )

    conn.commit()
    conn.close()

    print("Student added.")


def edit_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = input("Enter Student ID: ")

    # Check if the student exists
    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("Student not found.")
        conn.close()
        return

    print(f"\nCurrent Name : {student[1]}")
    print(f"Current Score: {student[2]}")

    print("\nWhat would you like to edit?")
    print("1. Student Name")
    print("2. Score")
    print("3. Both")

    choice = input("Choose: ")

    if choice == "1":
        new_name = input("New Student Name: ")

        cursor.execute(
            """
            UPDATE students
            SET student_name = ?
            WHERE id = ?
            """,
            (new_name, student_id)
        )

    elif choice == "2":
        new_score = input("New Score: ")

        cursor.execute(
            """
            UPDATE students
            SET scores = ?
            WHERE id = ?
            """,
            (new_score, student_id)
        )

    elif choice == "3":
        new_name = input("New Student Name: ")
        new_score = input("New Score: ")

        cursor.execute(
            """
            UPDATE students
            SET student_name = ?, scores = ?
            WHERE id = ?
            """,
            (new_name, new_score, student_id)
        )

    else:
        print("Invalid choice.")
        conn.close()
        return

    conn.commit()
    conn.close()

    print("Student updated successfully.")


def delete_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = input("Student ID: ")

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    print("Student deleted.")


def student_menu():
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. View Students")
        print("2. Add Student")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            view_students()

        elif choice == "2":
            add_student()

        elif choice == "3":
            edit_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Logged out.")
            break

        else:
            print("Invalid choice.")