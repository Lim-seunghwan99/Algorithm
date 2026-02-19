fst = input()
snd = input()
# fst = 'ACAYKP'
# snd = 'CAPCAK'
N = len(fst)
M = len(snd)
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
  for j in range(1, M + 1):
    if fst[i - 1] == snd[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[i][j])