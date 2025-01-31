# 3_Write a Python program to remove the  n-th index character from a nonempty string.

# Sample string: ‘abcdefgh’
# n = 3
# Expected result: abcefgh

my_str = "abcdefgh"
n = 3
new_str = my_str[:n] + my_str[n+1:]
print(new_str)