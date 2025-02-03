# Function Exercise:
# Write a function that checks if a given string is a valid email address.

import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return re.match(email_regex, email) is not None

print(is_valid_email("hovakimyankatrin16@gmail.com"))
