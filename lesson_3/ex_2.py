# 2_Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. ??
# If the string length of the given string is less than 3, leave it unchanged. ??

# Sample String : 'abc'
# Expected Result : 'abcing'

my_str = "abc"
if len(my_str) >=3:
    new_str = my_str + "ing"
print(new_str)

my_str = "abc"
if my_str[-3:] == "ing":
    new_str = my_str + "ly"
print(new_str)
