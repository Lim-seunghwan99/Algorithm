def boj1197():
    # 간선의 수가 많으므로 크루스칼 알고리즘을 쓴다.
    V, E = map(int, input().split())
    edge = []
    for i in range(E):
        a, b, c = list(map(int, input().split()))
        edge.append([a, b, c])
    edge.sort(key=lambda x: x[2])  # c를 기준으로 정렬

    parents = [i for i in range(V+1)]

    def find(x):
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return

        if x < y:
            parents[y] = x

        else:
            parents[x] = y

    cnt = 0
    sv = 0
    for a, b, c in edge:
        if find(a) != find(b):
            cnt += 1
            sv += c
            union(a, b)
            # MST 구성이 끝나면
            if cnt == V:
                break
    print(sv)


boj1197()