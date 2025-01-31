# BIRTH YEAR
# 7_The program prompts the user their birth year.
# Assuming a person’s age is a non-negative integer not exceeding 120,
# output the user’s age or the words “IncorrectYear”.
# The sample outputs assume it’s currently the year 2016.
# If you are writing this program during any other year,
# the correct answers may differ.
# Store the value of the current year in a variable.


current_year = 2024
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

if age < 0 or age > 120:
    print("IncorrectYear")
else:
    print("Your age is:", age)