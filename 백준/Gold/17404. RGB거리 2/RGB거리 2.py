N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

# 0번 집을 각각 R, G, B로 칠했을 경우를 모두 시도
for fst in range(3):
    dp = [[float('inf')] * 3 for _ in range(N)]

    # 첫 번째 집의 색을 고정
    dp[0][fst] = costs[0][fst]

    # 두 번째 집부터 DP 계산
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    # 마지막 집의 색깔은 첫 번째 집의 색깔과 달라야 함
    for lst in range(3):
        if fst != lst:
            ans = min(ans, dp[N-1][lst])

print(ans)