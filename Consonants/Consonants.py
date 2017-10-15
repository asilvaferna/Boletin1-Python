def consonantFinderIn(word):
    vocals = ["a", "e", "i", "o", "u"]

    strippedWord = word.replace(" ", "").lower()

    consonants = str()

    for letter in strippedWord:
        if letter in vocals:
            continue
        else:
            consonants += letter

    print(consonants)

consonantFinderIn("ADIOS")
