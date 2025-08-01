from collections import deque

T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    times = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1
    win = int(input())

    # 건물 win을 짓는데 드는 최소시간 구하기
    # 역순으로 가면 될 듯함.
    visited = [0] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
            visited[i] = times[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            visited[i] = max(visited[i], visited[now] + times[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    print(visited[win])

