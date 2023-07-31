def swea1966():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        for i in range(N - 1, 0, -1):
            for k in range(i): # N이 들어가면 오류 발생한다.
                if arr[k] > arr[k + 1]:
                    arr[k], arr[k + 1], = arr[k + 1], arr[k]
        print(f'#{tc}', *arr)


print(swea1966())