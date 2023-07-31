def swea1206():
    for tc in range(1, 11):
        n = int(input())
        arr = list(map(int, input().split()))
        count = 0
        for k in range(2, n-1):# n = arr[99] =0 arr[98] =0
            s = []
            if arr[k] > arr[k+1] and arr[k] > arr[k+2] and arr[k] > arr[k-1] and arr[k] > arr[k-2]: #255에서 에러난듯?
                s.append(arr[k] - arr[k + 1])
                s.append(arr[k] - arr[k + 2])
                s.append(arr[k] - arr[k - 1])
                s.append(arr[k] - arr[k - 2])
                count += min(s)
                # 카운트에서 세대 계산해야함, 위의 값 차들 다 구해서 min값을 ++
        print(f'#{tc} {count}')


swea1206()