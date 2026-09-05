x = input("Zahl: ")
summe = 0

while x != "":
    x = float(x)
    summe = summe + x
    x = input("Zahl: ")

print(f"Die Summe der Zahlen ist {summe}")