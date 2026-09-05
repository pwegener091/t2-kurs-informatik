# Funktion zählt für wie viele Zahlen zwischen 1 und 100 gilt, dass
# die Zahl k ohne Rest teilbar ist. Wir zählen die Teiler von k
def count_divisors(k):
    number = 0
    for i in range(1,101):
        if k % i == 0:
            number += 1
    return number

# Am Anfang sind alle Türen geschlossen.
# Für jeden Teiler wird der Zustand der Tür von geschlossen zu offen
# (oder umgekehrt) geändert.

tueren = []

for j in range(1,101):
    if count_divisors(j) % 2 == 0:
        tueren.append(False)
    else:
        tueren.append(True)


for i in range(100):
    if tueren[i]:
        print(f"Tür {i+1} ist offen.")