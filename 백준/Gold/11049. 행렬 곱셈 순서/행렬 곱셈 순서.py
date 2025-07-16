import sys
input = sys.stdin.readline

def boj11049():
    N = int(input())

    arr = []
    for i in range(N):
        r, c = list(map(int, input().split()))
        arr.append([r, c])

    dp = [[0] * N for _ in range(N)]

    for length in range(1, N):
        for i in range(N - length):
            j = i + length
            dp[i][j] = float('inf')

            for k in range(i, j):
                cst = dp[i][k] + dp[k + 1][j] + (arr[i][0] * arr[k][1] * arr[j][1])
                if dp[i][j] > cst:
                    dp[i][j] = cst

    print(dp[0][N-1])

if __name__ == "__main__":
    boj11049()