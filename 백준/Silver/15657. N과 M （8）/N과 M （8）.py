def f(i):
    global ans
    if i == M:
        for i in range(M-1):
            if res[i] <= res[i+1]:
                continue
            else:
                return
        print(*res)
        return
    for k in range(N):
        res.append(arr[k])
        f(i+1)
        res.pop()


N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
res = []
f(0)


