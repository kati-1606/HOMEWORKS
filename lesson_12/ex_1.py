# 1_Check Pangram Function
# Write a function that checks if a sentence is a pangram.

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return False
    return True

print(is_pangram("hjasvchjvsiak"))