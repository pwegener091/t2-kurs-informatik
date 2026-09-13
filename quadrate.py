"""
Erstelle aus einer Zahlenreihe range(1, 11) ein Dictionary quadrat_gerade,
bei dem nur für gerade Zahlen das Quadrat der Zahl als Wert gespeichert wird (Schlüssel: Zahl,
Wert: Quadratzahl).
"""

quadrat_gerade = {x: x**2 for x in range(2,11, 2)}

print(quadrat_gerade)