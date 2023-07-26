def ball_3():
    N, M = list(map(int, input().split()))
    t = [i for i in range(1, N+1)]
    for _ in range(M):
        i, j = list(map(int, input().split()))
        w = t[i-1:j] # k = 2 1435
        a = list(reversed(w))
        d = t[:i-1]
        c = t[j:]
        t = []
        t.extend(d)
        t.extend(a)
        t.extend(c)

    print(*t)
ball_3()