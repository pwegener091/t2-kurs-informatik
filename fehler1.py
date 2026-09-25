def berechne_durchschnitt(zahlen):

    summe = 0
    for zahl in zahlen:
        summe += zahl

    durchschnitt = (summe / len(zahlen)) + 1

    return durchschnitt

meine_zahlen = [10, 20, 30]
print(berechne_durchschnitt(meine_zahlen))