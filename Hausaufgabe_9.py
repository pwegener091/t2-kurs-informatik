produkte = [
"Laptop",
"Maus",
"Tastatur",
"FEHLER",
"Monitor",
"Maus",
"Tablet",
"ALT",
"Drucker",
"FEHLER",
"Scanner",
"Webcam",
"ALT",
"Lautsprecher",
"Mikrofon"
]

# (a)
for i in range(len(produkte)):
    if produkte[i] == "FEHLER":
        produkte[i] = "Unbekannt"

# (b)
while "ALT" in produkte:
    produkte.remove("ALT")

#produkte = [x for x in produkte if x != "ALT"]

# (c)
produkte.append("SSD")
produkte.append("Grafikkarte")

# (d)
produkte.insert(produkte.index("Webcam"), "Headset")

# (e)
for a in range(len(produkte)-1,-1,-1):
    for b in range(a):
        if produkte[a] == produkte[b]:
            del produkte[a]
            break

# (f)

for i in range(len(produkte)):
    print(f"{i+1}. {produkte[i]}")
