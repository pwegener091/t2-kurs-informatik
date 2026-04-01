def generate_email(vorname, nachname, firma):
    vorname = vorname.lower()
    nachname = nachname.lower()
    firma = firma.lower()
    print(f"{vorname}.{nachname}@{firma}.de")

#generate_email("Max", "Mustermann", "TechCorp")


def clean_text(satz, wort):
    satz = satz.replace(wort, "*"*len(wort))
    print(satz)

#clean_text("Alle Studierenden lieben das Fach Informatik", "Informatik")

def get_initials(name):
    # die Methode .split() liefert zwei Werte
    vorname, nachname = name.title().split()
    print(f"{vorname[0]}.{nachname[0]}.")

#get_initials("frank steinmeier")

def get_year(code):
    id, year, kategorie = code.split("-")
    return year

print(get_year("8271-2023-ELEC"))

