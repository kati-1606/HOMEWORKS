# 2_Print a square pattern using a nested for loop.
# The pattern should have 5 rows and 5 columns.

square = ""
for row in range(5):
    for col in range(5):
        square = "*" * 5
    print(square)


