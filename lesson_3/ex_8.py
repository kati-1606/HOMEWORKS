# 8_Create a string made of the first, middle and last character of given string with odd number of symbols

# Sample = ‘Sevak’
# Expected ‘Svk’

my_str = "Sevak"                                        #only for this case
new_str = my_str[0] + my_str[int(len(my_str)/2):int(len(my_str)/2)+1] + my_str[-1]
print(new_str)

#or

my_str = "Sevak"
if len(my_str) % 2 == 1:
    mid_index = len(my_str) // 2
    new_str = my_str[0] + my_str[mid_index] + my_str[-1]
    print(new_str)
else:
    print("The string must have an odd number of characters.")