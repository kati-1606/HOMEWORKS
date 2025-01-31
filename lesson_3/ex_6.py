# 6_Write a Python function to get a string made of its first three characters of a specified string. \
# If the length of the string is less than 3 then return the original string.

# Sample ='python'
# Expected pyt


my_str = "python"
if len(my_str) < 3:
    new_str = my_str
else:
    new_str = my_str[:3]
print(new_str)

# Sample ='python'
# Expected pyt

my_str = "py"
if len(my_str) < 3:
    new_str =  my_str
else:
    new_str = my_str[:3]
print(new_str)