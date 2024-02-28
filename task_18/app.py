import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet
result = is_pangram("The quick brown fox jumps over the lazy dog")
print(result)