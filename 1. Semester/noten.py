punkte = int(input("Punktzahl: "))  # punkte == 73

if punkte >= 90 and punkte <=100:  #  False and True == False
    print("Note: 1")
elif punkte >= 80 and punkte < 90:  #   False and True == False
    print("Note: 2")
elif punkte >= 70 and punkte < 80:  #   True and True == True 
    print("Note: 3")
elif punkte >= 60 and punkte < 70:
    print("Note: 4")
elif punkte >= 50 and punkte < 60:
    print("Note: 5")
else:
    print("Note: 6")