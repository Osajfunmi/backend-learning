# Simple backend simulation

# Fake database (dictionary)
users = {}

# Signup function
def signup(username, password):
    if username in users:
        return "Username already exists!"
    users[username] = password
    return "Signup successful!"

# Login function
def login(username, password):
    if username not in users:
        return "User does not exist!"
    if users[username] != password:
        return "Incorrect password!"
    return "Login successful!"

while True:
    print("\n--- Menu ---")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        u = input("Enter username: ")
        p = input("Enter password: ")
        print(signup(u, p))

    elif choice == "2":
        u = input("Enter username: ")
        p = input("Enter password: ")
        print(login(u, p))

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
