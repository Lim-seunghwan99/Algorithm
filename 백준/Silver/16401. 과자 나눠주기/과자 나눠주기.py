def boj16401():
    M, N = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # M명의 조카가 있고, N개의 과자가 있을 때 조카 1명에게 줄 수 있는 막대 과자의 최대 길이는?
    # arr을 나눠서 최대 길이
    left = 1
    right = max(arr)
    res = 0

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for x in arr:
            if x < mid:
                continue
            else:
                cnt += x // mid

        if cnt >= M:
            left = mid + 1
            res = mid
        else:
            right = mid - 1
    print(res)



if __name__ == "__main__":
    # boj15665()
    # boj16987()
    # boj5427()
    # boj13549()
    # boj18869()
    boj16401()