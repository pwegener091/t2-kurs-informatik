a = int(input("Was ist a? "))
b = int(input("Was ist b? "))
c = int(input("Was ist c? "))

# wir rechnen x und y aus
x = -b/(2*a)
y = (4*a*c-b**2)/(4*a)

print(f"Der Scheitelpunkt ist ({x}|{y})")