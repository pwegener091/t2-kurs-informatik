def finde_haeufigstes_element(liste):
    haeufigkeit = {}

    for element in liste:
        if element in haeufigkeit:
            haeufigkeit[element] += 1
        else:
            haeufigkeit[element] = 1
            
    meist_gesehen = None
    max_anzahl = 0

    for element in haeufigkeit:
        if haeufigkeit[element] > max_anzahl:
            max_anzahl = haeufigkeit[element]
            meist_gesehen = element
            
    return meist_gesehen, max_anzahl
    
daten = [ "Birne", "Apfel", "Apfel", "Zitrone", "Birne", "Apfel", "Birne"]
print(finde_haeufigstes_element(daten))