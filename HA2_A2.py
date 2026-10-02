def berechne_kassenbon(artikel_preise):

    gesamtsumme = 0
    
    for preis in artikel_preise:
        if preis >= 30:
            preis = preis - preis * 0.2
            
        gesamtsumme = gesamtsumme + preis
        
    return f"Bitte zahlen Sie: {gesamtsumme} Euro."

warenkorb = [12.50, 40.00, 15.00, 50.00]
print(berechne_kassenbon(warenkorb))
# Ausgabe ist nun korrekt: Bitte zahlen Sie: 99.5 Euro.