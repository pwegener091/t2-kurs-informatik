L = [ 1, 12, 13, 23, 44, 55, 56 , 60, 77]

#for i in range(len(L)):
#    if L[i] == 55:
#        print(i)
#        break

def index_rekursiv(liste, zahl, index=0): # index ist ein default value
    if liste[index] == zahl:
        return index
    else:
        return index_rekursiv(liste, zahl, index +1)


print(index_rekursiv(L, 55))











