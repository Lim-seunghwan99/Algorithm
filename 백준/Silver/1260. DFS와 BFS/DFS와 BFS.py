def bfs(n):
    q = [n]
    visited[n] = 1
    while q:
        t = q.pop(0)
        visited[t] = 1
        print(t, end=' ')
        for r in arr[t]:
            if visited[r] == 0:
                q.append(r)
                visited[r] = visited[t] + 1



def dfs(n):
    visited[n] = 1
    print(n, end=' ')
    for k in arr[n]:
        if visited[k] == 1:
            continue
        dfs(k)


N, M, v = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited =[0] * (N+1)  # 0이면 방문한적 없다.
for i in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
for i in range(len(arr)):
    arr[i].sort()
stack = []
dfs(v)
visited =[0] * (N+1)  # 0이면 방문한적 없다.
print()
bfs(v)