# LINE SEGMENT INTERSECTION
# 12_You are given four real numbers- a1, b1, a2, b2-
# The endpoints of two line segments on a line.
# Find the length of their intersection.
# Note that the order of the endpoints of a segment is irrelevant,
# i.e. the segments [1;2]
# and [2;1] are considered the same.


a1 = float(input("Enter the first endpoint of the first segment: "))
b1 = float(input("Enter the second endpoint of the first segment: "))
a2 = float(input("Enter the first endpoint of the second segment: "))
b2 = float(input("Enter the second endpoint of the second segment: "))
if a1 > b1:
    start1 = b1
    end1 = a1
else:
    start1 = a1
    end1 = b1

if a2 > b2:
    start2 = b2
    end2 = a2
else:
    start2 = a2
    end2 = b2

if end1 < start2 or end2 < start1:
    intersection_length = 0
elif start1 <= start2 and end1 >= end2:
    intersection_length = end2 - start2
elif start2 <= start1 and end2 >= end1:
    intersection_length = end1 - start1
elif start1 <= start2 <= end1:
    intersection_length = end1 - start2
elif start2 <= start1 <= end2:
    intersection_length = end2 - start1
else:
    intersection_length = 0

print("Length of the intersection:", intersection_length)