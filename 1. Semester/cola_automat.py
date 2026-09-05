# Cola kostet 80 Cents, Automat akzeptiert 50, 20, 10 und 5 Cents

preis = 80
summe = 0 # die Summe der bisher eingegebenen Münzen

while summe < preis:
    print(f"{80 - summe} Cents fehlen noch.")
    einwurf = int(input("Werfen Sie bitte Münzen ein: "))
    if einwurf in [5,10,20,50]:
        summe += einwurf # man kann auch summe = summe + einwurf
    else:
        print("Geben Sie bitte einen korrekten Wert ein.")

print("Hier ist ihre Cola.")
print(f"Sie bekommen {summe - 80} Cents zurück.")