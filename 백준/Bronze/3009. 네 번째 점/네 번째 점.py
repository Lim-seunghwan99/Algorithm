def completRectangle():
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    e, f = list(map(int, input().split()))
    if a == c:
        x = e
        if b == d:
            y = f
            print(x, y)
        elif b == f:
            y = d
            print(x, y)
        elif d == f:
            y = b
            print(x, y)
    elif a == e:
        x = c
        if b == d:
            y = f
            print(x, y)
        elif b == f:
            y = d
            print(x, y)
        elif d == f:
            y = b
            print(x, y)
    elif c == e:
        x = a
        if b == d:
            y = f
            print(x, y)
        elif b == f:
            y = d
            print(x, y)
        elif d == f:
            y = b
            print(x, y)
completRectangle()