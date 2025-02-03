# 2_Count all letters, digits,
# and special symbols from a given string

# 1_version
my_string = "P@#yn26at^&i5ve"
chars_count = 0
digits_count = 0
symbol_count = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

for char in my_string:
    if char in letters:
        chars_count += 1
    elif char in digits:
        digits_count += 1
    else:
        symbol_count += 1


print(f"chars = {chars_count} digits = {digits_count} symbol = {symbol_count}")


# 2_version
my_string = "P@#yn26at^&i5ve"
chars_count = 0
digits_count = 0
symbol_count = 0

for char in my_string:
    if char.isalpha():
        chars_count += 1
    elif char.isdigit():
        digits_count += 1
    else:
        symbol_count += 1

print(f"chars = {chars_count} digits = {digits_count} symbol = {symbol_count}")


# 3_version

my_string = "P@#yn26at^&i5ve"
chars_count = 0
digits_count = 0
symbol_count = 0

for char in my_string:
    if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
        chars_count += 1
    elif '0' <= char <= '9':
        digits_count += 1
    else:
        symbol_count += 1

print(f"chars = {chars_count} digits = {digits_count} symbol = {symbol_count}")
