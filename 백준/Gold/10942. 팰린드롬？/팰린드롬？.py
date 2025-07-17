import sys
input = sys.stdin.readline
import pprint

def boj10942():
    N = int(input())
    arr = list(map(int, input().split()))

    # 미리 전부 계산해두면 각 질문에 대해 O(1) 시간에 답할 수 있음
    # 양 끝의 두 수가 같고, 그 안쪽의 부분 수열이 팰린드롬이면 전체가 팰린드롬이다.
    dp = [[False] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = True

    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = True

    for length in range(3, N + 1):
        for start in range(N - length + 1):
            end = start + length - 1
            if arr[start] == arr[end] and dp[start + 1][end - 1]:
                dp[start][end] = True
    M = int(input())
    for _ in range(M):
        S, E = list(map(int, input().split()))
        if dp[S - 1][E - 1]:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    boj10942()