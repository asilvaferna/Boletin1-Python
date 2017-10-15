def isSorted(tuple):

    sortedTuple = sorted(tuple)

    if list(tuple) == sortedTuple:
        return True
    else:
        return False

tupla = (1, 8, 7)

print(isSorted(tupla))
