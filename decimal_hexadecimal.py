x = int(input("Dezimalzahl: "))
r = ""

zahlen = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"} 

while x > 0:
    rest = x % 16
    if rest < 10:
        r = str(rest) + r
    else:
        r = zahlen[rest] + r
    x = x // 16

print(f"Hexadezimalzahl ist {r}")