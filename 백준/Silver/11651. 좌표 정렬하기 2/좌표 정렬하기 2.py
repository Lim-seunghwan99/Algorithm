def baek11651():
    N = int(input())
    arr = []
    for _ in range(N):
        [x, y] = list(map(int, input().split()))
        arr.append([y, x])
    arr.sort()
    for i in range(len(arr)):
        arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
    for i in range(len(arr)):
        print(*arr[i])


baek11651()