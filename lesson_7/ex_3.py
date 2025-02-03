# 3_Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced
# if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.

string_1 = "Ya"
string_2 = "PYnative"
balanced = True
for char in string_1:
    if char not in string_2:
        balanced = False
print(balanced)

