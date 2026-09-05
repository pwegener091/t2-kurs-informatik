gaeste = ["Max", "Anna", "Lukas", "Anna", "Sophie", "Max", "Jonas", "Lukas"]

gaeste2 = []

for gast in gaeste:
    if gast not in gaeste2:
        gaeste2.append(gast)

print(gaeste2)

entferne = input("Name: ")

if entferne in gaeste2:
    gaeste2.remove(entferne)
else:
    print(f"{entferne} ist nicht in der Liste.")

print(gaeste2)
