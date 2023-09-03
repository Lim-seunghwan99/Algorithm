N = int(input())
time = []
arr = [i for i in range(N)]
for i in range(N):
    T, P = map(int, input().split())
    time.append([T, P])
res = 0
dp = [0] * (N+1)
for i in range(N+1):
    for j in range(i):
        # j 번째 날에서 일을 안하고 i 번째 날까지 온 경우
        dp[i] = max(dp[i], dp[j])

        # j번째 날에서 t[j]기간 동안 일을 하고 보상을 받은 경우
        if j + time[j][0] == i:
            dp[i] = max(dp[i], dp[j] + time[j][1])
    res = max(res, dp[i])
print(res)