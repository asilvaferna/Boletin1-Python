def sortedListBy(numberK, list):
    equalK = []
    lowerK = []
    upperK = []
    for number in list:
        if number == numberK:
            equalK.append(number)
        elif number < numberK:
            lowerK.append(number)
        else:
            upperK.append(number)

    return(equalK, lowerK, upperK)

lista = [5, 6, 7, 1, 3, 4, 2, 0, 10, 3000, 4, 100, 300, 4]

print(sortedListBy(4, lista))
