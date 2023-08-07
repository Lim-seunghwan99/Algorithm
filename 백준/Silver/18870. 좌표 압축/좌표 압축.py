def cordinate():
    N = int(input())
    arr = list(map(int, input().split()))
    t = list(sorted(set(arr)))
    d = {t[i]:i for i in range(len(t))}
    for i in arr:
        print(d[i], end=' ')
    # arr = 2 4 - 10 4 -9
    # arr을 정렬하면
    # -10 -9 2 4 4
    # -9보다 작은 값은 1
    # 자기보다 작은 값을 가진다
    # 2 3 0 3 1
    # arr = 1000 999 1000 999 1000 999
    # 결과값 1 0 1 0 1 0 중복부분 없애야 한다
cordinate()