# SMALLEST
# 3_Write a Python program to get the smallest number from a list

my_list = [1, 2, 3, 4]
min_num = my_list[0]
for num in my_list:
    if num < min_num:
        min_num = num
print("The smallest number in the list is:", min_num)