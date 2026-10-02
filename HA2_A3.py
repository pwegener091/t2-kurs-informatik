mensa_gerichte = [
    "Spaghetti Bolognese", # Index 0 (Tag 1)
    "Veganes Curry",       # Index 1 (Tag 2)
    "Schnitzel mit Pommes",# Index 2 (Tag 3)
    "Milchreis",           # Index 3 (Tag 4)
    "Fischstäbchen"        # Index 4 (Tag 5)
]

try:
    tag = float(input("Gib den Tag als Zahl ein (1-5): "))

    index = tag - 1

    gericht = mensa_gerichte[index]
except IndexError:
    print("Diesen Tag gibt es nicht!")
except ValueError:
    print("Bitte Zahl eingeben")
else: 
    print("Heute gibt es:", gericht)
finally:
    print("Ende.")

