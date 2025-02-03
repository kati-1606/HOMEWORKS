# Dictionaries Exercise:
# Write a function that finds the key with the maximum value in a dictionary.

def find_max_value_key(d):
    max_key = max(d, key=lambda k: d[k])
    return max_key

sample_dict = {
    "apple": 50,
    "banana": 75,
    "cherry": 100,
}

max_key = find_max_value_key(sample_dict)
print(f"The key with the maximum value is: '{max_key}'")

