# 1_String Length Checker
# Write a function that checks the length of a string provided by the user.
# Handle the TypeError by raising a custom exception if the input is not a string.
from sys import exception


def check_string_length(input_value):
    try:
        if not isinstance(input_value, str):
            raise exception("Input is not a string!")
        return len(input_value)

    except exception as e:
        print(f"Error: {e}")
        return None


print(f"Length of the valid string: {check_string_length(user_input)}")

