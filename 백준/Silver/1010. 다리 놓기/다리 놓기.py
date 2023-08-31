T = int(input())
for _ in range(T):
    N, k = map(int, input().split())
    N, k = k, N
    # McN을 구하란 거 같다...
    sv = 1
    i = 0
    t = k
    if N // 2 < k:
        k = N - k
    while i < k:
        sv *= (N - i)
        i += 1
    aaa = 1
    while k >= 1:
        aaa *= k
        k -= 1
    if t == 0:
        sv = 1
    else:
        sv //= aaa
    print(sv)