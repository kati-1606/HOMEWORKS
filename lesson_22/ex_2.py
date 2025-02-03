# 2_Character Frequency:
# Given a string, create a dictionary where keys are characters
# and values are their frequencies in the string.

my_string = "hello world"
frequency = {char: my_string.count(char) for char in my_string}
print(frequency)
