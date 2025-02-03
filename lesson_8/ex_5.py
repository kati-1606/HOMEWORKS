# 5_You are given three lists, list1, list2, and list3.
# Your task is to implement a programm that takes these lists and prints the following:

# The set of elements that are common to all three lists.
# The set of elements that are present in at least two of the three lists, but not in all three.
# The set of elements that are unique to each list (present in only one list)

list_1 = [1, 2, 3, 1, 5, 6, 3]
list_2 = [2, 8, 4, 4, 5, 6, 9]
list_3 = [1, 2, 5, 6, 5, 8, 4]

set_1 = set(list_1)
set_2 = set(list_2)
set_3 = set(list_3)

common_elements = set_1 & set_2 & set_3
at_least_two = (set_1 & set_2 | set_1 & set_3 | set_2 & set_3) - common_elements
unique_to_each = (set_1 - set_2 - set_3) | (set_2 - set_1 - set_3) | (set_3 - set_1 - set_2)

print("Set of elements common to all three lists:", common_elements)
print("Set of elements present in at least two of the three lists, but not in all three:", at_least_two)
print("Set of elements unique to each list:", unique_to_each)
