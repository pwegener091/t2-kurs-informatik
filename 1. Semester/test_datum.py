from datum import konnvertiere_datum

def main():
    test_normalfall()
    test_einstellig()
    test_fehler()
    print("Alle Tests bestanden")

def test_normalfall():
    assert konnvertiere_datum("11/13/2026") == "2026-11-13"

def test_einstellig():
    assert konnvertiere_datum("1/2/2026") == "2026-01-02"

def test_fehler():
    try:
        konnvertiere_datum("11/32/2026")
    except ValueError:
        pass
    else:
        assert False, "zu viele Tage"


if __name__ == "__main__":
    main()