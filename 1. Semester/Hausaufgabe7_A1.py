while True:
    zahl = int(input("Zahl eingeben: "))
    if zahl > 1:
        break

teiler = 0

for i in range(2, zahl):
    if zahl % i == 0:
        teiler += 1
        break

if teiler == 0:
    print(f"{zahl} ist eine Primzahl.")
else:
    print(f"{zahl} ist keine Primzahl.")
    print(f"{i} ist Teiler.")
    