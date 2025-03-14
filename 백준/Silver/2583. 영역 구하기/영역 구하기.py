from collections import deque
import pprint
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
M, N, K = list(map(int, input().split()))
# 둘째 줄부터 K 개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x,y 좌표값이 빈칸을 사이에 두고 주어진다.
visited = [[False] * N for _ in range(M)]
# 직사각형 방문처리
for _ in range(K):
    x1, y1, x2, y2 = list(map(int, input().split()))
    # 1. 직사각형을 돌면서 전부 방문처리?
    # 조건 넣는게 시간 절약 할 수 있으나, 오히려 오래 걸릴 수도.
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = True

# 방문체크
def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = True
    cnt = 1
    while q:
        v = q.popleft()
        x, y = v[0], v[1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx, ny])
                cnt += 1
    return cnt


ans = 0
ans_lst = []
for i in range(M):
    for j in range(N):
        if visited[i][j] is False:
            ans += 1
            ans_lst.append(bfs([i, j]))
print(ans)
print(*sorted(ans_lst))