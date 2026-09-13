zaehler = 0

def fibonacci(n):
    global zaehler
    zaehler += 1
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(35))
print(zaehler)