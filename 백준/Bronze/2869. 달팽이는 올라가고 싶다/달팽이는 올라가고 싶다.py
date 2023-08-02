def snail():
    A, B, V = list(map(int, input().split()))
    end = V - B
    x = end / (A-B)
    if x == int(x):
        print(int(x))
    else:
        print(int(x) + 1)

snail()