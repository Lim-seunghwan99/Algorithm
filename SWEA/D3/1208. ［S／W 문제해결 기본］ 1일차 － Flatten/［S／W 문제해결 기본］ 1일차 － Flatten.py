def sweaFlatten():
    for tc in range(1, 11):
        N = int(input())
        arr = list(map(int, input().split()))
        for i in range(N):  # 덤프 횟수만큼 덤프해라
            # 덤프는 어떻게? max -> min값으로 1만큼
            arr[arr.index(max(arr))] = arr[arr.index(max(arr))] - 1
            arr[arr.index(min(arr))] = arr[arr.index(min(arr))] + 1
            if max(arr) - min(arr) <= 1:
                break
        print(f'#{tc} {max(arr) - min(arr)}')
 
 
sweaFlatten()