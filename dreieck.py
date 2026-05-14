a = int(input("Seitenlänge des Dreiecks: "))

for i in range(a):
    print(" "*i, end = "")
    print("# "*(a-i))
