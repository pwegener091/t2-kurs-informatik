startbudget = 50
budget = startbudget
preis = -1

while budget > 0 and preis != 0:
    print(f"Sie haben noch {budget} Euro übrig.")
    preis = float(input("Preis des Artikels: "))
    if preis < 0:
        print("Ungueltiger Preis!")
    elif preis <= budget:
        budget = budget - preis
    elif preis > budget:
        print("Das ist zu teuer!")

print(f"Sie haben von {startbudget} Euro noch {budget} Euro übrig.")