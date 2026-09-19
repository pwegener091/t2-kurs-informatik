def hanoi(n, start, ziel, hilfe):
    if n == 1:
        print(f"Ziehe von Stapel {start} zu {ziel}")
    else:
        hanoi(n-1, start, hilfe, ziel)
        print(f"Ziehe von Stapel {start} zu {ziel}")
        hanoi(n-1, hilfe, ziel, start)

hanoi(3, "A", "C", "B")