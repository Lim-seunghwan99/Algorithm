def pprime():
    M = int(input())
    N = int(input())
    res = []
    for i in range(M, N+1):
        cnt = 0
        j = 1
        while j <= i:
            if i % j == 0:
                cnt += 1
            j += 1
        if cnt == 2:
            res.append(i)
    if len(res) == 0:
        print(-1)
    else:
        print(sum(res))
        print(min(res))


pprime()