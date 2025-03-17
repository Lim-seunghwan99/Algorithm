def boj15656():
    N, M = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    ans = []
    def back(idx):
        if len(ans) == M:
            print(*ans)
            return

        for i in range(idx, len(arr)):
            ans.append(arr[i])
            back(0)
            ans.pop()
    back(0)

if __name__ == "__main__":
    # boj9935()
    # boj1182()
    # boj15655()
    boj15656()