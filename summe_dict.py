ausgaben = {
    "Personal": 15000,
    "Marketing": {
        "Social Media": 1200,
        "Printmedien": 800
        },
    "Forschung_und_Entwicklung": {
        "Software": {
            "Lizenzen": 3500,
            "Cloud-Server": 2100
            },
        "Hardware": 4000
        },
    "Vertrieb": 5000
}

test = {"a": 5, "b": 7, "c": {"d": 2, "e": {"f:": 4, "g": 1}}}

def summe(D): # berechnet die Summe der Einträge in L
    ergebnis = 0
    for x in D.values():  # x = {"d": 2, "e": 5}
        if isinstance(x, dict):
            ergebnis += summe(x)
        else:
            ergebnis += x
    return ergebnis

print(summe(ausgaben))