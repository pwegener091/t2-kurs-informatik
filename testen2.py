def durchschnitt(zahlen):
    summe = 0

    for zahl in zahlen:
        summe += zahl
    durchschnitt = (summe / len(zahlen))
    return durchschnitt

#meine_zahlen = [10, 50, 30]
#print(durchschnitt(meine_zahlen))

def test_durchschnitt():
    assert durchschnitt([3,5,4]) == 4.0, f"Ergebnis: {durchschnitt([3,5,4])}, erwartet: 4.0"
    assert durchschnitt([-3,-5,-4]) == -4.0
    assert durchschnitt([0]) == 0.0
    assert durchschnitt([6]) == 6.0
    try:
        durchschnitt([])
    except ZeroDivisionError:
        pass
    else:
        assert False
    print("Alle Tests bestanden.")

test_durchschnitt()