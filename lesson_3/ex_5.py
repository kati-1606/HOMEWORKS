# 5_Write a Python function to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2).

# Sample =  "Python"
# Expected onononon

my_str = "Python"
new_str = 4 * my_str[-2:]
print(new_str)