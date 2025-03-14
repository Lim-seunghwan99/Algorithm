from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 어떤 지역의 높이 정보를 파악, 물에 잠기지 않는 안전한 지역이 최대로 몇개가 만들어 지는가?
# 높이를 한칸 씩 올리면서 계산?
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
mx = max(map(max, arr))
def bfs(start, chk):
    q = deque([start])
    visited[start[0]][start[1]] = True
    while q:
        v = q.popleft()
        x, y = v[0], v[1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and arr[nx][ny] > chk:
                visited[nx][ny] = True
                q.append([nx, ny])



ans = 0
for height in range(0, mx + 1):
    visited = [[False] * N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and arr[i][j] > height:
                tmp += 1
                bfs((i, j), height)
    ans = max(tmp, ans)
print(ans)

