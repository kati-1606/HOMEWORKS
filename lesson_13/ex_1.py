# 1_Write a Python program to square and cube every number
# in a given list of integers using Lambda.

squares = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
cubes = list(map(lambda x: x**3, [1, 2, 3, 4, 5]))
print("Squares:", squares, "Cubes:", cubes)
