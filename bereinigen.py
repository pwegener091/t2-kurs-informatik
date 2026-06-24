eingaben = ["", "", "Avatar", "", "", "Bild.png", "", "Text.txt"]
i = 0
while i < len(eingaben):
    if eingaben[i] == "":
        eingaben.pop(i)
        continue
    i += 1
print(f"Bereinigte Eingaben: {eingaben}")