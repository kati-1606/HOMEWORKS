# 4_Character ASCII Values:
# Given a string, create a dictionary where keys are characters,
# and values are their ASCII values.

my_string = "hello world"
ascii_values = {char: ord(char) for char in my_string}
print(ascii_values)