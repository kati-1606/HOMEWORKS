# 9_Append new string in the middle of a given (even number of characters) string

# Sample = ‘python’
# new_string = ‘new’
# Expected ‘pytnewhon'

my_str = "abcdefgh"
new_str = "new"
mid_index = len(my_str)//2
last_str = my_str[:mid_index] + new_str + my_str[mid_index:]
print(last_str)