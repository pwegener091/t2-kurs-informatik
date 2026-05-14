summe = 0  

while True: 
    x = int(input("Geben Sie bitte eine Zahl ein: "))
    if x == 0:
        break
    elif x > 0:
        summe += x

print(f"Die Summe ist {summe}.")