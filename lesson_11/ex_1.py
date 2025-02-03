# 1_Max of Three
# Write a Python function to find the Max of three numbers.

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
result = max_of_three(8, 10, 3)
print(result)
