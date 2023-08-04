def triangleexcreta():
    while True:
        res = []
        a, b, c = list(map(int, input().split()))
        res.append(a)
        res.append(b)
        res.append(c)
        sorted(res)
        if a == b == c == 0:
            break
        if res[0] + res[1] <= res[2]:
            print('Invalid')
        elif a == b == c:
            print('Equilateral')
            continue
        elif a == b or a == c or b == c:
            print('Isosceles')
            continue
        elif a != b != c:
            print('Scalene')
            continue


triangleexcreta()