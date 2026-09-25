while True:
    n = input("Bitte Zahl eingeben: ")
    if n.isnumeric():
        print(int(n)*4)
        break
    else: 
        print("Das war keine Zahl")