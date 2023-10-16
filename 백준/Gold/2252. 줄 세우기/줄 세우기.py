def boj2252():
    from collections import deque
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
    in_degree = [0] * (N + 1)
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            in_degree[arr[i][j]] += 1

    q = deque()
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
            visited[i] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(len(arr[x])):
            in_degree[arr[x][i]] -= 1
            if in_degree[arr[x][i]] == 0:
                q.append(arr[x][i])


boj2252()