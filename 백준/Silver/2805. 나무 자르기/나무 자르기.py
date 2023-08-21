def sangun():
    N, M = map(int, input().split())  # 나무의 수 N, 가져가고자 하는 나무의 길이 M
    arr = list(map(int, input().split()))
    mi = 1
    mx = max(arr)
    while mi <= mx:
        mid = (mi+mx) // 2
        sv = 0
        for i in arr:
            if i - mid < 0:
                sv += 0
            else:
                sv += i - mid
        if sv >= M:
            mi = mid + 1
        else:
            mx = mid - 1
    print(mx)

sangun()