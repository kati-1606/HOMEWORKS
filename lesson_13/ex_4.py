# 4_Write a Python program to find intersection
# of two given arrays using Lambda.

# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays:  [1, 2, 8, 9]

array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
find_intersection = list(filter(lambda x: x in array_nums1, array_nums2))
print(find_intersection)