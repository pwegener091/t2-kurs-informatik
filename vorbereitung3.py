def t(n):
    if n < 3:
        return 1
    return t(n - 1) + t(n - 3)

print(t(7))

