# 1_Print the even numbers from 0 to 20 using a for loop and the range function

even_numbers = []
for i in range(21):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)