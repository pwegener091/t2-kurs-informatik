zaehler = 0
fib = {1:1, 2:1}

def fibonacci(n):
    global zaehler
    zaehler += 1
    if n in fib:
        return fib[n]
    else:
        f = fibonacci(n-1)+fibonacci(n-2)
        fib.update({n:f})
        return f

print(fibonacci(4))
print(fib)
print(zaehler)