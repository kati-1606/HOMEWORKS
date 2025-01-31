# DIGIT SUM
# 3_Input a two-digit natural number and output the sum of its digits.
# You can assume that the input will be a two-digit number and need not check that programmatically

num = int(input())
first_digit = num // 10
second_digit = num % 10
sum = first_digit + second_digit
print(sum)