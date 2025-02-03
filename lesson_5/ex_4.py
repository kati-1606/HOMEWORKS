# SECOND SMALLEST
# 4_Write a Python program to find the second smallest number in a list.

my_list = [1, 2, 3, 4]
if my_list[0] < my_list[1]:
    min_num = my_list[0]
    second_min_num = my_list[1]
else:
    min_num = my_list[1]
    second_min_num = my_list[0]

for num in my_list[2:]:
    if num < min_num:
        second_min_num = min_num
        min_num = num
    elif num != min_num and num < second_min_num:
        second_min_num = num
print(second_min_num)