dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(s, e):
    q = [(s, e)]
    arr[s][e] = 1
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:
                arr[ny][nx] = arr[y][x] + 1
                q.append((nx, ny))


N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for i in range(N):
    a = input()
    for j in range(len(a)):
        arr[i][j] = int(a[j])
bfs(0, 0)
print(arr[N-1][M-1])