def boj15655():
    # N 개의 자연수 중에 M개를 고른 수열
    N, M = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    ans = []
    def recursion(s):
        if len(ans) == M:
            print(*ans)
            return

        for i in range(s, N):
            ans.append(arr[i])
            recursion(i + 1)
            ans.pop()
    recursion(0)


if __name__ == "__main__":
    # boj9935()
    # boj1182()
    boj15655()