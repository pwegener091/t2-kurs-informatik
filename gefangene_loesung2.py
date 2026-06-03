tueren = [False]

tueren = tueren*100  # Liste mit 100 Einträgen, alle Einträge sind False

for i in range(0,100): # i ist der aktuelle Durchlauf, Schleife läuft von 1 bis 100
    for j in range(i,100,i+1): # j ist die aktuelle Tür
        if tueren[j] == True:
            tueren[j] = False
        else:
            tueren[j] = True

for i in range(len(tueren)):
    if tueren[i] == True:
        print(f"Tür {i+1} ist auf.")