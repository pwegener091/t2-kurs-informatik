L = [1, 2, [3, [4, 5, [6, 7], 8], 9]]

def summe(L): # berechnet die Summe der Einträge in L
    ergebnis = 0
    for x in L:
        if isinstance(x, list) == True:
            ergebnis += summe(x)
        else:
            ergebnis += x
    return ergebnis

print(summe(L))
