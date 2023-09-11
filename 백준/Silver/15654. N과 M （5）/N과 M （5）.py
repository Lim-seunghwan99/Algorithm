def f(i):
    if i == M:
        temp = []
        for k in range(i):
            temp.append(arr[k])
        res.append(temp)
        return
    for j in range(i, N):
        arr[i], arr[j] = arr[j], arr[i]
        f(i+1)
        arr[i], arr[j] = arr[j], arr[i]


N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
res = []
f(0)
res.sort()
for i in range(len(res)):
    print(*res[i])