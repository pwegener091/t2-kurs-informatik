tueren = [1]
tueren = tueren * 100
tueren.insert(0, None) 

for zelle in range(1,101): # Nummern der Zellen
    for durchgang in range(2,101): # Nummer des Durchgangs
        if zelle % durchgang == 0: 
            if tueren[zelle] == 0:
                tueren[zelle] = 1
            else:
                tueren[zelle] = 0

for i in range(1,101):
    if tueren[i] == 1:
        print(f"Tür {i} ist auf.")