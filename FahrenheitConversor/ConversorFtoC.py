def convertFtoC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print("%.2f" % celsius)

def convertFtoCAutoTable():
    fahrenheit = 0
    while fahrenheit <= 120:
        celsius = (fahrenheit - 32) * 5 / 9
        print("ºF: ", fahrenheit,  " -> ºC: ", "%.2f" % celsius)
        fahrenheit += 10

convertFtoC(100)
convertFtoC(0)
convertFtoCAutoTable()
