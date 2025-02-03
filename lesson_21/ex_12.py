# List Exercise:
# Write a function that returns the nth largest element from a list.

def nth_largest_element(lst, n):
    unique_lst = sorted(set(lst), reverse=True)

    if n <= 0 or n > len(unique_lst):
        return "Invalid value of n."

    return unique_lst[n - 1]


lst = [10, 20, 4, 45, 99, 99, 20]
n = 3
result = nth_largest_element(lst, n)

if isinstance(result, int):
    print(f"The {n}rd largest element is: {result}")
else:
    print(result)

