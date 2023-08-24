import sys
sys.setrecursionlimit(10**5)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def year(i, j):
    cnt = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr2[nx][ny] == 0:
            cnt += 1
    arr[i][j] -= cnt
    if arr[i][j] < 0:
        arr[i][j] = 0


def check(i, j):
    global ans
    q = [(i, j)]
    while q:
        i, j = q.pop(0)
        visited[i][j] = 1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] > 0 and visited[nx][ny] == 0:
                check(nx, ny)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 0이 붙어있는 범위만큼 줄어든다.
# 이거를 두개로 나뉘어 질 떄 까지 반복한다.
# 나누어져 있는 빙산 체크
arr2 = [arr[i][:] for i in range(N)]  # 깊은 복사 확인함
res = 0
while True:
    res += 1
    cnt2 = 0  # 다 녹는거 체크하기 위해서
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                year(i, j)
            if arr[i][j] == 0:
                cnt2 += 1

    if cnt2 == N * M:
        res = 0
        break
    #print(arr)
    arr2 = [arr[i][:] for i in range(N)]  # 깊은 복사 확인함
    ans = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and visited[i][j] == 0:
                check(i, j)
                ans += 1
    if ans >= 2:
        break


print(res)


