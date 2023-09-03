N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
M, k = map(int, input().split())
arr2 = []
for j in range(M):
    arr2.append(list(map(int, input().split())))
res = [[0] * k for _ in range(N)]
for i in range(N):
    for r in range(M):
        for j in range(k):
            res[i][j] += arr[i][r] * arr2[r][j]
for o in range(N):
    print(*res[o])