x = input("Zahl: ")

def quersumme(x):
    summe = 0
    if len(x) > 1:
        summe += int(x[0]) ** quersumme(x[1:])
        return summe
    else:
        summe =+ int(x)
        return summe

print(quersumme(x))


