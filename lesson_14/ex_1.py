# 1_Character Count:
# Write a Python script that reads a text file (input.txt) and counts the
# occurrences of each character (including spaces and punctuation).
# Output the character frequency to another text file (output.txt)

with open("input.txt", "r") as file:
    text = file.read()

char_counts = {}
for char in text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

with open("output.txt", "w") as file:
    file.write("Character Frequency Count:\n")
    for key,value in char_counts.items():
        file.write(f"{key}:{value}\n")
print(f"Character frequency count has been written to 'output.txt'.")
