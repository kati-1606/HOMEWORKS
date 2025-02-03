# 5_Sum of Squares Function
# Write a function that calculates the sum of squares of numbers from 1 to n.

def sum_of_squares(numbers):
    sum = 0
    for element in numbers:
        sum += element ** 2
    return sum
print(sum_of_squares(range(1, 5)))

