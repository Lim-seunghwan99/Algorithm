def boj1774():
    def find(x):
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(a, b):
        na = find(a)
        nb = find(b)

        if na > nb:
            parents[na] = nb
        else:
            parents[nb] = na

    def dist(a, b):
        return ((a[0] - b[0])**2 + (a[1]-b[1]) ** 2) ** 0.5

    N, M = map(int, input().split())
    arr = []
    cor = []
    parents = [i for i in range(N)]
    for i in range(N):
        x, y = map(int, input().split())
        cor.append((x, y))
    for j in range(M):
        x, y = map(int, input().split())
        union(x-1, y-1)
    for i in range(N-1):
        for j in range(i+1, N):
            arr.append((i, j, dist(cor[i], cor[j])))
    arr.sort(key=lambda k: k[2])
    sv = 0
    for s, e, w in arr:
        if find(s) != find(e):
            union(s, e)
            sv += w
    print(f'{sv:.2f}')


boj1774()