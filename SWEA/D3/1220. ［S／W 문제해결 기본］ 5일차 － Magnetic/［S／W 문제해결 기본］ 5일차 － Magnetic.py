T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1은 N극 아래로 떨어진다. 더 큰 S극 행값이 있으면 멈춘다.
    # 2는 S극 위로 떨어진다. 더 작은 N극 행값이 있으면 멈춘다.
    # res2[0] > res1[-1] :
    cnt = 0
    for i in range(N):
        res1 = []
        res2 = []
        for j in range(N):
            if arr[j][i] == 1:
                res1.append(j)
            elif arr[j][i] == 2:
                res2.append(j)
        while res2:
            a = res2.pop(0)
            x = 0
            chk = 0
            while True:
                if len(res1) > x and res1[x] > a:
                    break
                if len(res1) > x and res1[x] < a:
                    chk += 1
                    x += 1
                else:
                    break
            if chk > 0:
                cnt += 1
            while chk > 0:
                res1.pop(0)
                chk -= 1
    print(f'#{tc} {cnt}')