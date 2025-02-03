# 9_Print Prime Numbers Function
# Write a function that prints all prime numbers up to a given limit.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_prime_numbers(limit):
    for i in range(2, limit + 1):
        if is_prime(i):
            print(i)

get_prime_numbers(20)