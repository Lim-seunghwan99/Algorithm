def remain():
    res = []
    for i in range(10):
        num = int(input())
        k = num % 42
        if k not in res:
            res.append(k)
    return len(res)
print(remain())