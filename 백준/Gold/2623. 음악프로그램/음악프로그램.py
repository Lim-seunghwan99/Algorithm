from collections import deque

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1):
        u, v = arr[i], arr[i + 1]
        graph[u].append(v)
        in_degree[v] += 1


def topological_sort(graph, in_degree, n):
    result = []
    q = deque()

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for neighbor in graph[now]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    if len(result) == n:
        return result
    else:
        return 0


ans = topological_sort(graph, in_degree, N)
if ans == 0:
    print(0)
else:
    for i in ans:
        print(i)
