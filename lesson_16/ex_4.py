# 4_Login System
# Write a simple login system where the user enters a username and password.
# Handle the KeyError by raising a custom exception if the username is not
# found in the users database(dictionary).

def login_system(username, password, users_db):
    try:
        if username not in users_db:
            raise KeyError(f"Error: Username '{username}' not found.")

        if users_db[username] != password:
            raise ValueError("Error: Incorrect password.")

        return "Login successful!"

    except KeyError as e:
        return e

users_db = {
    "user1": "password123",
    "user2": "mypassword",
    "admin": "adminpass",
}

username = input("Enter username: ")
password = input("Enter password: ")

print(login_system(username, password, users_db))

