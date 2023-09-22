def boj6497():
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
    while True:
        m, n = map(int, input().split())  # 집의 수 m, 길의 수 n
        if m == 0 and n == 0:
            break
        parents = [i for i in range(m)]
        graph = []
        mx_sv = 0
        for i in range(n):
            x, y, z = map(int, input().split())
            graph.append((x, y, z))
            graph.append((y, x, z))
            mx_sv += z
        graph.sort(key=lambda k: k[2])
        sv = 0
        MST = []
        for s, t, w in graph:
            if find(s) != find(t):
                union(s, t)
                MST.append((s,t,w))

        for a, b, c in MST:
            sv += c
            #print(a, b, c)
        #print(sv)
        #print(mx_sv)
        print(mx_sv-sv)


boj6497()