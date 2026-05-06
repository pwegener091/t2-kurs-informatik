a = float(input("Zahl: "))
# Nach der Genauigkeit fragen
d = float(input("Genauigkeit: "))

x_alt = (a+1)/2

abstand = d

while abstand >= d:
    x_neu = x_alt - (x_alt ** 2 - a)/(2 * x_alt)
    # Betrag von x_neu - x_alt
    abstand = abs(x_neu - x_alt)
    x_alt = x_neu

print(f"Die Wurzel von {a} ist näherungsweise {x_neu}.")