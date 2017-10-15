from collections import Counter

def countWords(string):
    words = string.split()
    return dict(Counter(word for word in words))

print(countWords("Qué lindo día que fai hoxe que que que"))
