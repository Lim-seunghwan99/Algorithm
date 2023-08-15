import sys
sys.setrecursionlimit(10 ** 6)
def dfs(arr, v, visited):
    global cnt
    visited[v] = cnt
    for i in arr[v]:
        if visited[i]==0:
            cnt += 1
            dfs(arr, i, visited)


N, M, R = map(int,sys.stdin.readline().split())
visited = [0] * (N + 1)
arr = [[] for _ in range(N+1)]
cnt = 1
for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(N+1):
    arr[i].sort(reverse=True)

dfs(arr, R, visited)
for i in range(N+1):
    if i != 0:
        print(visited[i])