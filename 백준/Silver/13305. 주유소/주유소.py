def gasstation2():
    n = int(input())
    arr = list(map(int, input().split()))  # 도로의 길이 키로당 1리터
    pr = list(map(int, input().split()))  # 리터당 가격

    res = 0
    m = pr[0]
    for i in range(n-1):
        if pr[i] < m:
            m = pr[i]
        res += m * arr[i]
    print(res)
gasstation2()