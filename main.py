from Backend.auth.login import register_user, login_user

print("1 - Register")
print("2 - Login")

choice = input("Choose: ")

if choice == "1":
    username = input("Username: ")
    password = input("Password: ")

    result = register_user(username, password)
    print("Registered:" if result else "Failed")

elif choice == "2":
    username = input("Username: ")
    password = input("Password: ")

    result = login_user(username, password)
    print("Login successful" if result else "Login failed")