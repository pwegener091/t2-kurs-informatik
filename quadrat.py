def quadrat(x):
    return x ** 2

def test_quadrat():
    assert quadrat(3) == 9, f"Ergebnis: {quadrat(3)}, erwartet: 9"
    assert quadrat(0) == 0
    assert quadrat(-3) == 9
    assert quadrat(1.5) == 2.25
    print("Alle Tests bestanden.")

test_quadrat()