N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
res = []
while len(arr) > 1:
    for i in range(K):
        if i == K-1:
            res.append(arr.pop(0))
        else:
            arr.append(arr.pop(0))
res.append(arr[0])
print('<', end='')
print(*res, sep=', ', end='>')