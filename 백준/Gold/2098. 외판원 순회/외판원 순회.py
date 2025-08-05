# 외판원 순회
# 1 ~ N번 까지 도시를 모두 거쳐 원래의 도시로 돌아오는 순회 여행 경로 계획
N = int(input())
weights = [[]]
for _ in range(N):
    weights.append([0] + list(map(int, input().split())))
dp = [[float('inf')] * (1 << N) for _ in range(N + 1)]

start = 1
dp[start][1 << (start - 1)] = 0

for mask in range(1, 1 << N):
    for j in range(1, N + 1):
        # 현재 조합에 j번 도시가 포함되지 않으면 건너뛴다.
        if not (mask & (1 << (j - 1))):
            continue

        # 오기 직전의 도시에 대하여
        for k in range(1, N + 1):
            # 같은 도시거나 직전의 도시가 포함되어 있지 않으면 pass
            if k == j or not (mask & (1 << (k-1))):
                continue

            # j번 도시를 방문하기 전 상태 마스크
            prev = mask ^ (1 << (j - 1))

            if  weights[k][j] != 0 and dp[k][prev] != float('inf'):
                dp[j][mask] = min(dp[j][mask], dp[k][prev] + weights[k][j])

ans = float('inf')
for i in range(2, N + 1):
    if weights[i][1] != 0:
        tmp = dp[i][(1 << N) - 1] + weights[i][1]
        ans = min(ans, tmp)
print(ans)