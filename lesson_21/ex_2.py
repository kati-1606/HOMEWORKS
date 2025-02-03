# Class Exercise:
# Create a Python class representing a basic calculator with methods
# for addition, subtraction, multiplication, and division.

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Cannot divide by zero.")
        return self.value / other.value

calc1 = Calculator(10)
calc2 = Calculator(5)

print(calc1 + calc2)
print(calc1 - calc2)
print(calc1 * calc2)
print(calc1 / calc2)

