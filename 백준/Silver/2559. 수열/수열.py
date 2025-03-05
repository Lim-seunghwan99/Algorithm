N, K = map(int, input().split())
days = list(map(int, input().split()))

sv = sum(days[:K])  # 첫 K일의 합
ans = sv  # 최댓값을 첫 구간 합으로 초기화

for i in range(K, N):
    sv = sv - days[i - K] + days[i]  # 슬라이딩 윈도우 적용
    ans = max(ans, sv)  # 최댓값 갱신

print(ans)
