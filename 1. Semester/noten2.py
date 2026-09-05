punkte = int(input("Punktzahl: "))  # punkte == 73

if 90 <= punkte:  #  False and True == False
    print("Note: 1")
elif 80 <= punkte:  #   False and True == False
    print("Note: 2")
elif 70 <= punkte:  #   True and True == True 
    print("Note: 3")
elif 60 <= punkte:
    print("Note: 4")
elif 50 <= punkte:
    print("Note: 5")
else:
    print("Note: 6")