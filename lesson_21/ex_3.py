# List Exercise:
# Given a list of numbers, write a function to find the sum of all numbers
# in the list that can be divided by 7.

def sum_divisible_by_7(numbers):
    #total_sum = sum([number for number in numbers if number % 7 == 0])
    filtered_numbers = []
    for number in numbers:
        if number % 7 == 0:
            filtered_numbers.append(number)
    total_sum = sum(filtered_numbers)
    return total_sum

numbers = [14, 21, 35, 50, 49, 12, 28]
result = sum_divisible_by_7(numbers)
print(f"The sum of numbers divisible by 7 is: {result}")



