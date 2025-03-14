from collections import deque
T = int(input())
# 나이트가 이동하려는 칸이 주어질 때, 나이트가 몇 번 움직이면 이 칸으로 이동할 수 있을까?
# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫 줄은 체스판의 한 변의 길이
# 둘째 줄에는 나이트가 현재 있는 칸 셋째 줄에는 나이트가 이동하려는 칸
dx = [1, -1, 2, 2, -2, -2, 1, -1]
dy = [2, 2, 1, -1, 1, -1, -2, -2]

def bfs(start, end, visited, chk):
    if start[0] == end[0] and start[1] == end[1]:
        return 0
    q = deque([[start[0],start[1], chk]])
    visited[start[0]][start[1]] = True
    while q:
        v = q.popleft()
        x, y, chk = v[0], v[1], v[2]
        for k in range(8):
            nx = dx[k] + x
            ny = dy[k] + y
            if nx == end[0] and ny == end[1]:
                return chk + 1
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==False:
                visited[nx][ny] = True # 방문체크
                q.append([nx, ny, chk + 1])

for t in range(T):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    visited = [[False] * n for _ in range(n)]
    print(bfs(start, end, visited, 0))