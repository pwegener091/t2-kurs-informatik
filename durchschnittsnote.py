noten = {"Anna": 1.3, "Ben": 2.7, "Clara": 1.0, "David": 3.3, "Elena": 1.7}

"""
Schreibe ein Python-Programm, das den Notendurchschnitt aller Studierenden berechnet und
alle Studierenden ausgibt, deren Note besser (d.h. kleiner) als der Durchschnitt ist
"""
L = []
for y in noten.values():
    L.append(y)

durchschnitt = sum(L)/len(L)
print(durchschnitt)

for x,y in noten.items():
    if y < durchschnitt:
        print(x)