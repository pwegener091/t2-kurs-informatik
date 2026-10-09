ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar(text, k):
    ergebnis = ""
    for zeichen in text.upper():
        if zeichen in ALPHABET:
            x = ord(zeichen) - ord("A") 
            y = (x + k) % 26
            ergebnis += chr(y + ord("A"))
        else:
            ergebnis += zeichen
    return ergebnis


#text = "ENDLICH WOCHENENDE!"
#print(caesar(text, 7))
#verschluesselt = "LUKSPJO DVJOLULUKL!"
#print(caesar(verschluesselt, -7))



geheim = "NSKTWRFYNP RFHMY XUFXX"

for k in range(26):
    print(caesar(geheim, k))