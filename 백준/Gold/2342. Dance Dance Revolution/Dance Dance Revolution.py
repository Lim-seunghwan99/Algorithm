import sys
input = sys.stdin.readline


def get_cost(current_pos, nxt_pos):
    # 1 -> 2, 4로 가면 3, 3으로 가면 4
    # 2 -> 1, 3로 가면 3, 4로 가면 4
    # 3 -> 2, 4로 가면 3, 1로 가면 4
    # 4 -> 1, 3로 가면 3, 2로 가면 4
    if current_pos == 0:
        return 2
    elif current_pos == nxt_pos:
        return 1
    elif abs(current_pos - nxt_pos) % 2 == 1:
        return 3
    else:
        return 4

def boj2342():
    arr = list(map(int, input().split()))
    N = len(arr) - 1

    # 왼발, 오른발을 움직일 수 있으므로 두칸 확인? 왼발을 움직였을때, 오른발을 움직였을 때
    dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for l in range(5):
            for r in range(5):
                if dp[i][l][r] == float('inf'):
                    continue
                dp[i + 1][arr[i]][r] = min(dp[i+1][arr[i]][r], dp[i][l][r] + get_cost(l, arr[i]))
                dp[i + 1][l][arr[i]] = min(dp[i + 1][l][arr[i]], dp[i][l][r] + get_cost(r, arr[i]))
    ans = float('inf')
    for i in range(5):
        for j in range(5):
            ans = min(ans, dp[N][i][j])
    print(ans)

if __name__ == "__main__":
    boj2342()