def main():
    euros = euros_to_float(input("Wie teuer war das Essen? "))
    prozent = prozent_to_float(input("Wie viel Prozent Trinkgeld wollen Sie geben? "))
    trinkgeld = euros * prozent
    print(f"Gib {trinkgeld:.2f} Euro Trinkgeld")

def euros_to_float(d): # d ist zum Beispiel der String "130,75€"
    d = d.replace("€", "")
    d = d.replace(",",".")
    return float(d)
    

def prozent_to_float(p): # p ist zum Beispiel 13%
    p = p.replace("%", "") 
    return float(p) / 100


main()