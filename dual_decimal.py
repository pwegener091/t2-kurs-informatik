x = input("Dualzahl: ")   # x = 1100100
# y soll die Dezimalzahl werden
y = 0 

#for i in range(len(x)):  # 0,1,2,3,4,5,6
#    y += int(x[i]) * (2**(len(x) -i-1))

for i in range(len(x)-1,-1,-1):  # 6,5,4,3,2,1,0
    y += int(x[len(x)-i-1]) * (2**i)

print(f"Die Dezimalzahl ist {y}")
