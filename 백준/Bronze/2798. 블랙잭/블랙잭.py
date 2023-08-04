def blackjack():
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    mx = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if arr[i] + arr[j] + arr[k] <= M:
                    sv = arr[i] + arr[j] + arr[k]
                    if mx < sv:
                        mx = sv
    print(mx)

blackjack()