# 5_Type Conversion:
# Write a function that prompts the user to enter a number and tries to convert it to an
# integer. Handle the TypeError exception by printing a message indicating that the input
# is not a valid number. Use a finally block to print "Type conversion process completed.

def convert_to_integer():
    try:
        user_input = int(input("Enter a number: "))
        print(f"The integer value is: {user_input}")
    except ValueError:
        print("The input is not a valid number.")
    finally:
        print("Type conversion process completed.")

convert_to_integer()
