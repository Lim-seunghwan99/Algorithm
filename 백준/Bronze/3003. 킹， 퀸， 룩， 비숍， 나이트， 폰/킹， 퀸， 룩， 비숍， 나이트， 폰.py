def chess():
    ch = list(map(int, input().split()))
    t = [1, 1, 2, 2, 2, 8]
    res = []
    for i in range(len(t)):
        if ch[i] != t[i]:
            res.append(t[i]-ch[i])
        else:
            res.append(0)
    return res
print(*chess())