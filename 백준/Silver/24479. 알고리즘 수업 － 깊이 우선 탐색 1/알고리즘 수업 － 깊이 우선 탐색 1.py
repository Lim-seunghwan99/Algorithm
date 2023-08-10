import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def dfs5(graphs,n,visited):
    global cnt
    visited[n] = cnt
    for m in graphs[n]:
        if visited[m] == 0:
            cnt += 1
            dfs5(graphs,m,visited)
N, M, R = map(int, input().split())
graphs = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1
for _ in range(M):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)
for i in range(N+1):
    graphs[i].sort()
dfs5(graphs, R, visited)
for i in range(N+1):
    if i!=0:
        print(visited[i])