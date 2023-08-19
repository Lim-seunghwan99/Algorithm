import sys
sys.setrecursionlimit(10000)
# 재귀에러 발생시
def check(i, j):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < M and 0 <= nj < N and arr[nj][ni] == 1: # 범위 M이다** # 범위 안에 있는 경우
            arr[nj][ni] = 0
            check(ni, nj)


T = int(sys.stdin.readline())
for tc in range(1, T+1):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, sys.stdin.readline().split())
        arr[j][i] = 1
    res = 0
    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:# 1을 찾고, 방문하지 않았다면,
                check(i, j)
                res += 1

    print(res)