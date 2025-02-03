# 6_Count Words Function
# Write a function that counts the number of words in a sentence

def count_words(sentence):
    return len(sentence.split())
print(count_words("I love python "))
