"""
Erstelle ein Dictionary wort_laengen, das nur Wörter der Liste woerter
enthält, die mindestens 5 Zeichen lang sind. Die Schlüssel sollen die Wörter in Großbuchstaben
sein und die Werte die jeweilige Länge des Wortes.
"""
woerter = ["Python", "Skript", "Tupel", "Dictionary", "Code", "Informatik", "KI"]

#wort_laengen = {}
#for wort in woerter:
#    if len(wort) > 4:
#        #wort_laengen[wort.upper()] = len(wort)
#        wort_laengen.update({wort.upper(): len(wort)})

wort_laengen = {wort.upper(): len(wort) 
                for wort in woerter 
                if len(wort)>4}

print(wort_laengen)