import random

def sumOfTwoDicesAfter(numberRolls):
    totalSum = 0
    for i in range(numberRolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        totalSum += dice1 + dice2

        print("Total: ", totalSum, " 1: ", dice1, " 2: " , dice2)

    return totalSum

numberRolls = 4
print("Suma total despues de %d tiradas:  " %numberRolls, sumOfTwoDicesAfter(numberRolls))
