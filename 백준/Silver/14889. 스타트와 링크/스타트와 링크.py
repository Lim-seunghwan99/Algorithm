import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
inf = 200000000
res = inf

def dfs(L, idx):
    global res
    if L == N//2:
        a = 0
        b = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    a += arr[i][j]
                elif not visited[i] and not visited[j]:
                    b += arr[i][j]
        res = min(res, abs(a-b))
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(L+1, i+1)
            visited[i] = False
dfs(0, 0)
print(res)