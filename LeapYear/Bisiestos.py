def isLeap(year):
    if year % 4 == 0 & year % 100 != 0:
        print("Is leap")
    elif year % 400 == 0:
        print("Is leap too")
    else:
        print("Is not leap")

isLeap(1600)

