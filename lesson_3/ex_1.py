 # 1_Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.

# Sample String : 'w3resource'
# Expected Result : 'w3ce'

my_str="w3resource"
new_str =  my_str[:2]+my_str[-2:]
print(new_str)

# Sample String : 'w3'
# Expected Result : 'w3w3'

my_str = 'w3'
new_str = 2 * my_str[:2]
print(new_str)

