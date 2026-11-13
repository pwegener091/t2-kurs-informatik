def main():
    while True:
        eingabe = input("Datum im Format MM/TT/JJJJ: ")
        try:
            print(konnvertiere_datum(eingabe))
            break
        except ValueError:
            print("Fehler. Bitte verwenden Sie das richtige Format.")

def konnvertiere_datum(eingabe):
    monat_str, tag_str, jahr_str = eingabe.split("/")

    m = int(monat_str)
    t = int(tag_str)
    j = int(jahr_str)
    if not (1 <= m <= 12 and 1 <= t <= 31 and 0 <= j<= 9999):
        raise ValueError("Ungültige Zahlenwerte")
        
    return f"{j:04d}-{m:02d}-{t:02d}"

if __name__ == "__main__":
    main()