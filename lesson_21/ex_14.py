# Strings Exercise:
# Write a function that capitalizes the first letter of each word in a sentence.

def capitalize_first_letter(sentence):
    return ' '.join([word.capitalize() for word in sentence.split()])

sentence = "hello world, this is a test sentence."
capitalized_sentence = capitalize_first_letter(sentence)
print(capitalized_sentence)
