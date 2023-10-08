def boj14442():
    import sys
    input = sys.stdin.readline
    from collections import deque

    def bfs():
        q = deque()
        q.append((0, 0, 0, 1))
        visited[0][0][0] = 1
        while q:
            x, y, z, final = q.popleft()
            # 이 식이 없으면 k 값이 클 경우에 처음 도착 한 값이 아닌 k번 파낸 값이
            # 최종값으로 결정된다.
            if x == N - 1 and y == M - 1:
                return final
            for r in range(4):
                nx = x + dx[r]
                ny = y + dy[r]
                if 0 <= nx < N and 0 <= ny < M:
                    # 벽을 부수지 않았고, 벽이 아닐 때,
                    if arr[nx][ny] == 1 and z < k and visited[z+1][nx][ny] == -1:
                        q.append((nx, ny, z+1, final+1))
                        visited[z+1][nx][ny] = 1
                    # 벽인 경우
                    elif arr[nx][ny] == 0 and visited[z][nx][ny] == -1:
                        q.append((nx, ny, z, final+1))
                        visited[z][nx][ny] = 1
        return -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N, M, k = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[[-1] * M for _ in range(N)] for _ in range(k+1)]
    ans = bfs()
    print(ans)


boj14442()