# 6_Dictionary Merge:
# Given two dictionaries, merge them into a new dictionary,
# excluding any keys that start with an underscore.

dict1 = {"_id": 1, "name": "Alice", "age": 25}
dict2 = {"_score": 100, "city": "New York", "country": "USA"}
merged_dict = {key: value for d in (dict1, dict2) for key, value in d.items() if not key.startswith('_')}
#merged_dict = {key: value for key, value in {**dict1, **dict2}.items() if not key.startswith('_')}
print(merged_dict)