N, K = map(int, input().split())
days = list(map(int, input().split()))
sv = sum(days[:K])
ans = sv

for i in range(K, N):
    # sv에서 이전 값 빼고, 이후 값 추가
    sv = sv - days[i - K] + days[i]
    if ans < sv:
        ans = sv
print(ans)