T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sv = 0
    for i in range(N//2+1):
        for j in range(N//2-i, N//2+1+i):
            sv += arr[i][j]
            sv += arr[N - i - 1][j]
    for k in range(N):
        sv -= arr[N//2][k]
    print(f'#{tc} {sv}')