#  5_Write a Python program to add two given lists
#  using map and lambda.(map-y kara function-ic
#  heto mekic avel hajordakanutyun ynduni, orinak erku list)

#  Original list:
#  [1, 2, 3]
#  [4, 5, 6]
#  Result: after adding two list
#  [5, 7, 9]

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
result_of_adding_two_lists = map(lambda x, y: x + y, nums1, nums2)
print(list(result_of_adding_two_lists))
