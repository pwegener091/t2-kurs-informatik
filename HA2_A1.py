def potenz(basis, exponent):
    if exponent == 0:
        return 1
    else:
        return basis * potenz(basis, exponent - 1)

print(potenz(4, 2))