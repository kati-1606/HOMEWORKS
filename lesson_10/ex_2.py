# 2_Write a Python program that asks the user to enter a password.
# Keep asking for the password until the correct password "secret" is entered.
# Provide appropriate feedback to the user.

correct_password = "secret"
password = input("Enter the password: ")
while password != correct_password:
    print("Incorrect password")
    password = input("Enter the password: ")
print("Correct password")