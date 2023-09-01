def bfs(r, i):
    if r == 0:
        print(*reversed(comb))
        return

    for j in range(i, k - r + 1):
        comb[r-1] = arr[j]
        bfs(r-1, j+1)


while True:
    arr = list(map(int, input().split()))
    k = arr.pop(0)
    if k == 0:
        break
    comb = [0] * 6
    bfs(6, 0)
    print()