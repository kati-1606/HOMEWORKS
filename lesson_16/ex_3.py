# 3_URL Validator
# Write a function that validates a URL string. Handle the ValueError by raising a custom
# exception if the URL format is invalid.

def validate_url(url):
    if not url.startswith(('http://', 'https://')):
        raise ValueError("Error: URL must start with 'http://' or 'https://'.")

    url_without_protocol = url.split('://', 1)[1]

    if '.' not in url:
        raise ValueError("Error: URL must contain a dot '.' in the domain name.")

    if ' ' in url:
        raise ValueError("Error: URL cannot contain spaces.")

    parts = url_without_protocol.split('.')

    for part in parts:
        if part == "":
            raise ValueError("Invalid URL: Domain parts cannot be empty.")

    if not parts[-1].isalpha():
        raise ValueError(f"Invalid URL: Domain part '{part}' must contain only alphabetic characters.")

url = "https://example.c1om"
try:
    validate_url(url)
    print("URL is valid.")
except ValueError as e:
    print(e)

