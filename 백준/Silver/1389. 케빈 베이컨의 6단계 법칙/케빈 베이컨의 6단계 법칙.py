def bfs(x):
    q = [x]
    while q:
        t = q.pop(0)
        for k in range(len(arr[t])):
            cur = arr[t][k]
            if visited[cur] == -1:
                q.append(cur)
                visited[cur] = visited[t]+1



N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    # 케빈 베이컨의 수가 가장 작은 사람을 출력 한다.
    arr[a].append(b)
    arr[b].append(a)
mn = 999999999
ans = 0
for i in range(1, N+1):
    visited = [-1] * (N+1)
    bfs(i)
    sv = sum(visited)
    if mn > sv:
        mn = sv
        ans = i
print(ans)
