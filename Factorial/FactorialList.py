def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)

def factorialList(list):
    list = [factorial(number) for number in list]
    return list


