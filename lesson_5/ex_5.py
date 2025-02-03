# DUPLICATES
# 5_Write a Python program to remove duplicates from a list

my_list = [1, 2, 3, 1]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)