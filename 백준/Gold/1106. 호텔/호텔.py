import sys
input = sys.stdin.readline


def boj1106():
    C, N = list(map(int, input().split()))
    cities = []
    for i in range(N):
        cities.append(list(map(int, input().split())))
    # 고객을 적어도 C명 늘이기 위해 투자해야 하는 돈의 최솟값
    dp = [float('inf')] * (C + 101)
    dp[0] = 0
    for cost, value in cities:
        for w in range(value, C + 101):
            dp[w] = min(dp[w], cost + dp[w - value])
    print(min(dp[C:]))


if __name__ == "__main__":
    boj1106()