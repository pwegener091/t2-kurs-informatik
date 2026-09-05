personen = {
    "Arya": "Stark",
    "Cersei": "Lannister",
    "Daenerys": "Targaryen",
    "Jaime": "Lannister",
    "Jon": "Stark" 
}

print(personen["Jon"])
personen["Jon"] = "Targaryen" # Jon aktualisiert
print(personen["Jon"])
personen["Tyrion"] = "Lannister" # Tyrion hinzufügen
print(personen)

for p in personen:
    if personen[p] == "Lannister":
        print(p)

del personen["Cersei"]
print(personen)
personen.update({"Cersei": "Lannister", "Ned": "Stark"})
print(personen)

for x,y in personen.items():
    if y == "Lannister":
        print(x)

