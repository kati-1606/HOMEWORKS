# Math Operations Exercise:
# Write a function that calculates the square root of a  number using the math module.

import math

def calculate_square_root(number):
    if number < 0:
        return "Error: Cannot calculate square root of a negative number."
    square_root = math.sqrt(number)
    return square_root

number = 16
result = calculate_square_root(number)
print(f"The square root of {number} is: {result}")
