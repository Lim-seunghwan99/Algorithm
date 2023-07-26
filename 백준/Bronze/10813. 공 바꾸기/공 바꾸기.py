def ball_2():
    N, M = list(map(int, input().split()))# N, M
    t = [i for i in range(1, N+1)]
    for _ in range(M):
        i, j = list(map(int, input().split())) # i = 1, j = 2
        if j-i < 1:
            k = t.pop(j-1) # 2번재 빼냄 [1,3,4,5], k = 2
            t.insert(i-1, k) #[2 1 4 3 5] [32145]
        else:
            k = t.pop(j - 1)
            t.insert(i - 1, k)
            k = t.pop(i)  # 2번재 빼냄 [1,3,4,5], k = 2
            t.insert(j - 1, k) #[32145] [3145]
    print(*t)
ball_2()