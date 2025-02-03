# 4_Write a Python function that takes two sets as input and returns a new set
# containing elements that are present in either of the input sets, but not in both.

set_1 = set(input("Enter elements for the first set:"))
set_2 = set(input("Enter elements for the second set:"))
new_set = set_1 ^ set_2
print(new_set)