ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def haeufigkeiten(text):
    zaehler = {}
    for zeichen in ALPHABET:
        zaehler[zeichen] = 0
    for zeichen in text.upper():
        if zeichen in ALPHABET:
            zaehler[zeichen] += 1
    return zaehler


def teilweise_entschluesseln(geheimtext, zuordnung):
    ergebnis = ""
    for zeichen in geheimtext:
        if zeichen in zuordnung:
            ergebnis += zuordnung[zeichen].lower()
        else:
            ergebnis += zeichen
    return ergebnis



text = """KTQQHXDYRDY QOVA ADY QLGMPDQQDM SP PVQDYDW AOCORTMDV MDJDV ADQGTMJ QXMMRD WTV QOD QXYCNTDMROC HTDGMDV DOV CPRDQ KTQQHXYR OQR MTVC PVA DVRGTDMR EDOVD HXDYRDY AOD OV
DOVDW HXDYRDYJPLG QRDGDV JDQXVADYQ QOLGDY QOVA MTVCD QTDRSD TPQ ADVDV WTV QOLG DOV
KTQQHXYR TJMDORDR ADVV AODQD ETVV WTV QOLG CPR WDYEDV PVA QOD QOVA RYXRSADW QLGHDY
SP DYYTRDV TPQQDYADW QXMMRD WTV NPDY BDADV AODVQR DOV DOCDVDQ KTQQHXYR IDYHDVADV"""
print(haeufigkeiten(text))

print(teilweise_entschluesseln(text, {"D": "E", "Y": "R", "A": "D", "O": "I", "V": "N", "T": "A", "R": "T", "P": "U", "Q": "S", "W": "M", "J": "B", "S": "Z", "L": "C", "G": "H", "N": "F", "I": "V", "K": "P", "H": "W", "E": "K", "C": "G", "M": "L", "X": "O"}))