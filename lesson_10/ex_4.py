# 4_Write a Python program that generates a random number
# between 1 and 100 and asks the user to guess the number.
# The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.

secret_number = int(input("Enter the secret number: "))

guess_number = int(input("Guess the secret number: "))
while guess_number != secret_number:
    if guess_number < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess_number = int(input("Guess the secret number: "))

print("You guessed the number!")
