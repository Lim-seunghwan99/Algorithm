import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

r = [0] * m # m으로 나눈 나머지 담는 곳
prefixSum = 0
for i in range(n):
    prefixSum += a[i]
    r[prefixSum % m] += 1

ans = r[0] # 나머지가 0이 되는 경우의 수
for i in range(m):
    # nC2 = n(n-1)/2
    ans += r[i] * (r[i]-1) // 2
print(ans)

# 나머지가 같은 두 개의 조합을 통해 구간 합을 구할 수 있다.