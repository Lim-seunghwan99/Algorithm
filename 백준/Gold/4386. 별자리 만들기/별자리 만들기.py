def boj4386():
    def find(x):
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        nx = find(x)
        ny = find(y)
        if nx < ny:
            parents[ny] = nx
        else:
            parents[nx] = ny

    n = int(input())
    x = []
    y = []
    for i in range(n):
        t_x, t_y = map(float, input().split())
        x.append(t_x)
        y.append(t_y)
    arr = []
    #print(f'x {x}')
    #print(f'y {y}')
    for i in range(n):
        for j in range(i + 1, n):
            a = (x[i] - x[j])
            b = (y[i] - y[j])
            arr.append([i, j, (a ** 2 + b ** 2) ** 0.5])
            #print([i, j, (a ** 2 + b ** 2)])

    arr.sort(key=lambda k: k[2])
    #print(arr)
    # 여기까지 그래프 생성 및 간선 가중치 기준 정렬

    parents = [i for i in range(len(arr))]
    MST = []
    for u, v, w in arr:
        if find(u) != find(v):
            MST.append((u, v, w))
            union(u, v)
    sv = 0
    for u, v, w in MST:
        sv += w
    print(round(sv, 2))
    
    
boj4386()