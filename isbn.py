zahl = input("Zahl eingeben: ")

zahl = zahl.replace("-","")
summe = 0

for i in range(len(zahl)):
    if i % 2 != 0:
        summe += int(zahl[i])*3
    else: 
        summe += int(zahl[i])

if summe % 10 == 0:
    print("ISBN Zahl ist richtig")
else:
    print("Falsche ISBN")

