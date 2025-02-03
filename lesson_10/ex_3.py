# 3_Write a Python program that calculates the sum of all even numbers
# between 1 and 100 using a while loop.

# version_1
x = 1
gumar = 0
while x <= 100:
    if x % 2 == 0:
        gumar += x
    x += 1
print(gumar)

# version_2
x = 0
gumar = 0
while x < 100:
    x += 2
    gumar += x
print(gumar)