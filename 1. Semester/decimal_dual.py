x = int(input("Dezimalzahl: "))
r = ""

while x > 0:
    r = str(x % 2) + r
    x = x // 2

print(r)
    