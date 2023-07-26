def ball():
    N, M = list(map(int, input().split()))
    t = [0] * N
    for _ in range(M):
        i, j, k = list(map(int, input().split()))
        for m in range(i-1, j):
            t[m] = k
    print(*t)


ball()