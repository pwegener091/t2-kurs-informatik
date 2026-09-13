def f(x):
    print(x)
    if x > 1:
        f(x/2)

f(100)