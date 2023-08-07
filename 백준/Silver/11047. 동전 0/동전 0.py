def restcoin():
    N, K = list(map(int, input().split()))
    coin = []
    cnt = 0
    for _ in range(N):
        arr = int(input())
        coin.append(arr)
    #while K == 0:
    for i in range(N-1, -1, -1):
        cnt += K // coin[i]
        K = K % coin[i]
    print(cnt)


restcoin()