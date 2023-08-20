import sys
sys.setrecursionlimit(10**7)
def findt(x, y):
    arr[x][y] = 0  # 확인한 쓰레기는 다시 확인하지 않는다.
    global cnt
    cnt += 1
    res.append(cnt)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
            findt(nx, ny)
N, M, K = map(int, input().split())  # N = 세로길이, M = 가로길이, K = 음식물 쓰래기 수
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

res = []
for x in range(N):
    for y in range(M):
        cnt = 0
        if arr[x][y] == 1:
            findt(x, y)
print(max(res))