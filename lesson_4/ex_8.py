# THREE NUMBERS
#  8_Input three integers.
#  Output the word “Sorted” if the numbers are listed in a non-increasing
#  or non-decreasing order and “Unsorted” otherwise.

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
if a <= b <= c or a >= b >= c :
    print("Sorted")
else:
    print("Unsorted")