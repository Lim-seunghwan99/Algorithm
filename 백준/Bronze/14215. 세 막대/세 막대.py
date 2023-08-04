def bigtriangle():
    a, b, c = list(map(int, input().split()))
    r = []
    r.append(a)
    r.append(b)
    r.append(c)
    r = sorted(r)
    if r[-1] >= r[0] + r[1]:
        r[-1] = (r[0] + r[1])-1
    print(sum(r))
bigtriangle()