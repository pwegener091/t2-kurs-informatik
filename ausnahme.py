try:
    n = float(input("Zahl eingeben: "))
except ValueError:
    print("Das war keine Zahl!")
else: 
    try:
        print(n/(n-5))
    except ZeroDivisionError:
        print("5 geht nicht! Nicht durch 0 teilen")
finally:
    print("Wochenende!")
