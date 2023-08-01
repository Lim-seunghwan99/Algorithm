def swea11092():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        min_idx = 0
        max_idx = 0
        for i in range(1, N):  # N + 1쓰면 오류 난다. why?
            if arr[min_idx] > arr[i]:
                # >, >= 차이 >=의 경우 오른쪽을 선택한다.
                min_idx = i
            if arr[max_idx] <= arr[i]:
                max_idx = i
        #res = abs(max_idx - min_idx)
        if max_idx > min_idx:
            res = max_idx - min_idx
        else:
            res = min_idx - max_idx
        print(f'#{tc} {res}')


swea11092()
