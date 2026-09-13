ergebnisse = [
("Alice", "Mathematik", 1.7),
("Bob", "Informatik", 2.3),
("Alice", "Informatik", 1.0),
("Charlie", "Mathematik", 3.0),
("Bob", "Mathematik", 2.0),
("Alice", "Physik", 1.3),
("Charlie", "Informatik", 2.7)
]

"""
Schreibe eine Funktion restrukturiere_daten(ergebnisse), die diese Daten in ein ver-
schachteltes Dictionary umwandelt. Der äußere Schlüssel soll der Schülername sein. Der innere
Wert soll wieder ein Dictionary sein, welches das Fach als Schlüssel und die Note als Wert
enthält.
Erstelle anschließend mithilfe von Dictionary Comprehension ein Dictionary durchschnitte,
welches jedem Schüler seinen Notendurchschnitt zuordnet.
"""

def restrukturiere_daten(ergebnisse):
    schueler = {}
    for name, fach, note in ergebnisse:
        if name not in schueler:
            schueler[name] = {}
        schueler[name][fach] = note

    durchschnitte = {
        name: round(sum(schueler[name].values())/len(schueler[name]), 2)
        for name in schueler
        }

    return durchschnitte


print(restrukturiere_daten(ergebnisse))

    