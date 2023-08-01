def baek11005():
    n, k = list(map(int, input().split()))
    res = []
    res2 = []
    while n > 0:
        i, m = divmod(n, k)
        n = i
        if m >= 10:
            m = chr(m + 55)
            res.append(m)
        else:
            res.append(str(m))
    for g in range(len(res)-1, -1, -1):
        res2.append(res[g])
    return res2


a = ''.join(baek11005())
print(a)