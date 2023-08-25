def check(i, j, k):
    cnt = 0
    for r in range(len(h_list)):
        sv = 0
        sv += abs(i - h_list[r][0])
        sv += abs(j - h_list[r][1])
        if sv < k:
            cnt += 1
    #print(cnt)
    return cnt
T = int(input())
#T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    h_list = []  # 집들의 위치 현 좌표와 비교해서 k안이면 cnt ++
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                h_list.append((i, j))
    k = 1
    mx = 0
    while k < N + 2:
        cost = k * k + (k - 1) * (k - 1)
        #print(cost)
        for i in range(N):
            for j in range(N):
                cur = check(i, j, k)
                if mx < cur and M * cur - cost >= 0:
                    #print(f' r {k} {M * cur - cost}')
                    mx = cur
        k += 1
    print(f'#{tc} {mx}')