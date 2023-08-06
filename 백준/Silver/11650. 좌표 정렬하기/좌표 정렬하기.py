def baek11650():
    N = int(input())
    arr = []
    for i in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x : (x[0], x[1]))
    for i in arr:
        x, y = i
        print(x,y)


baek11650()