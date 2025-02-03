# 2_Letters Count
# Write a Python function to calculate count of each letter in string

def count_letters(s):
    letter_count = {}
    for char in s:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count
result = count_letters('abrakadabra')
print(result)

