# 2_Find and Replace:
# Implement a Python program that reads a text file (input.txt),
# prompts the user for a word to find, and another word to replace it with.
# Replace all occurrences of the first word with the second word and save
# the modified text to a new file (output.txt)

with open("input.txt", "r") as file:
    text = file.read()

find_word = input("Enter the word to find: ")
replace_word = input("Enter the word to replace it with: ")

modified_text = text.replace(find_word, replace_word)

with open("output.txt", "w") as file:
    file.write(modified_text)

print("The file has been updated and saved as 'output.txt'.")
