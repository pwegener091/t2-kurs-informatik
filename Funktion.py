wertepaare = [(1,1,1), (1,2,1), (1,3,2), (2,1,3), (2,2,4), (2,3,5)]

def f(x,y,z):
    return x**2 + y**2 +z

for x,y,z in wertepaare:
    print(f(x, y,z))
