import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
def bfs(x, y):
    heap = []
    heapq.heappush(heap, (0, x, y))

    while heap:
        count, cx, cy = heapq.heappop(heap)
        visited[cx][cy] = True

        if cx == (n - 1) and cy == (n - 1):
            return count

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 1:
                    heapq.heappush(heap, (count, nx, ny))
                else:
                    heapq.heappush(heap, (count + 1, nx, ny))

print(bfs(0,0))