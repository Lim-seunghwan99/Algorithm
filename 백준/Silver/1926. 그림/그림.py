from collections import deque

n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

# 1로 연결된 것의 개수와, 가장 넓은 것의 넓이를 출력하라
# 가로나 세로로 연결이 된 것만 연결이 된 것이다.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * m for _ in range(n)]

def bfs(graph, node, visited):
    q = deque([node])
    visited[node[0]][node[1]] = True
    chk = 1
    while q:
        v = q.popleft()
        x, y = v[0], v[1]
        # 4분탐색을 해서 방문하지 않았고, 1이라면 q에 append
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx, ny])
                chk += 1
    return chk

cnt = 0
mx = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt += 1  # 개수 ++
            mx = max(mx, bfs(arr, [i, j], visited))
print(cnt, mx)

