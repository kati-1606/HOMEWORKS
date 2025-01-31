# 4_Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

# Sample: ‘abcdefgh’
# Expected: ‘hbcdefga

my_str = "abcdefgh"
new_str = my_str[-1] + my_str[1:-1] + my_str[0]
print(new_str)
