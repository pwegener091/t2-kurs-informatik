while True:
    eingabe = input("Bitte geben Sie ein Datum im Format MM/TT/JJJJ: ")

    try:
        monat, tag, jahr = eingabe.split("/")

        m = int(monat)
        t = int(tag)
        j = int(jahr)

        if 1<=m<=12 and 1<=t<=31:
            print(f"{j:04d}-{m:02d}-{t:02d}")
            break
        else:
            print("ungueltige Zahlenwerte")
    except ValueError:
        print("Bitte richtiges Format verwneden")


"""
10/16/2026
['10', '16', '2026']
2026-10-16
"""