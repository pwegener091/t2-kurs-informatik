def f(wort):
    if wort == "":
        return ""
    if wort[0] in "aeiou":
        return f(wort[1:])
    return wort[0] + f(wort[1:])

print(f("info"))