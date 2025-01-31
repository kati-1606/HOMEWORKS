# ROUNDING - 2
# 11_Given a real number, round it to the nearest whole.

number = float(input("Enter a real number: "))
decimal_part = number - int(number)
if decimal_part < 0.5:
    rounded_number = int(number)
else:
    rounded_number = int(number) + 1
print("Rounded number:", rounded_number)