# 5_Filtering Word Lengths:
# Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.

words_list = ["list", "set", "tuple", "dictionary", "number"]
lengths = {word: len(word) for word in words_list if len(word) > 3}
print(lengths)