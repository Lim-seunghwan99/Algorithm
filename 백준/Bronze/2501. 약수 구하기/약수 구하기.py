def baek2501():
    N, K = list(map(int, input().split()))
    arr = []
    for i in range(1, N+1):
        if N % i == 0:
            arr.append(i) # 오름차순 정렬
    if len(arr) >= K:
        print(arr[K-1])
    else:
        print(0)
baek2501()