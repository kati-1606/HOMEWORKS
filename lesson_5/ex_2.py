# LARGEST
# 2_Write a Python program to get the largest number from a list.

my_list = [1, 2, 3, 4]
max_num = my_list[0]
for num in my_list:
    if num > max_num:
        max_num = num
print("The largest number in the list is:", max_num)