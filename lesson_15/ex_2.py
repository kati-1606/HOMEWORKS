
# 2_RandomPassword Generator:
# Write a function that generates a random password for the user.
# Allow the user to specify the length and complexity of the password
# (include letters, numbers, and symbols).
# Ogtvel random u string module-neric (string.ascii_letters, string.digits,string.punctuation, )
import string
import random

def generate_password(length, character_set):
    password = []
    for i in range(length):
        random_char = random.choice(character_set)
        password.append(random_char)
    return ''.join(password)

length = int(input("Enter password length: "))
print('''Choose character set for password from these:
             1. Letters
             2. Digits
             3. Special characters
             4. Done''')

character_list = ""
while True:
        choice = int(input("Pick a number (1-4): "))
        if choice == 1:
            character_list += string.ascii_letters
            print("Letters added.")
        elif choice == 2:
            character_list += string.digits
            print("Digits added.")
        elif choice == 3:
            character_list += string.punctuation
            print("Special characters added.")
        elif choice == 4:
            break
        else:
            print("Please pick a valid option (1-4).")

if character_list:
    password = generate_password(length, character_list)
    if password:
        print(f"The random password is: {password}")
