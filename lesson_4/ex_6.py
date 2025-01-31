# COMPARISON
# 6_Input two positive integers, and output a line describing their relation.


a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))
if a > b:
    print(str(a) + " > " + str(b))
elif a < b:
    print(str(a) + " < " + str(b))
else:
    print(str(a) + " = " + str(b))