def f(i, k, sv):
    global cnt
    if i == N:
        if sv == k:
            cnt += 1
        return
    f(i+1, k, sv)
    f(i+1, k, sv+A[i])


T = int(input())
for tc in range(1, T+1):
    N, k = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    f(0, k, 0)
    print(f'#{tc} {cnt}')