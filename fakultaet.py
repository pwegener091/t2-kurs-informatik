#def fakultaet(n):
#    ergebnis = 1
#    for i in range(1,n+1):
#        ergebnis *= i
#    return ergebnis

def fakultaet(n):
    if n == 0: # Basisfall
        return 1
    return n*fakultaet(n-1)

print(fakultaet(200))

#print(fakultaet(49)/(fakultaet(43)*fakultaet(6)))
