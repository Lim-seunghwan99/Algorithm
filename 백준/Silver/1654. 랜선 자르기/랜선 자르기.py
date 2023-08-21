K, N = map(int, input().split())
sv = 0
arr = [int(input()) for _ in range(K)]
mid = sum(arr) // N
mi = 1
mx = max(arr)
while mi <= mx:  # 이분 탐색이 완료 될 때까지 반복
    mid = (mi+mx) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    if cnt >= N:
        mi = mid + 1
    else:
        mx = mid - 1
print(mx)