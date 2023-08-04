def land():
    n = int(input())
    res_x = []
    res_y = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        res_x.append(x)
        res_y.append(y)
    print((max(res_x)-min(res_x)) * (max(res_y)-min(res_y)))

land()