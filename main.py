from Backend.auth.login import register_user, login_user
from Backend.student import student_menu

print("1 - Register")
print("2 - Login")

choice = input("Choose: ")

if choice == "1":
    username = input("Username: ")
    password = input("Password: ")

    result = register_user(username, password)
    print("Registered!" if result else "Registration failed.")

elif choice == "2":
    username = input("Username: ")
    password = input("Password: ")

    result = login_user(username, password)

    if result:
        print("Login successful!")
        student_menu()      # Opens the student management menu
    else:
        print("Login failed.")