def countv():
    N = int(input())
    R = list(map(int, input().split()))
    v = int(input())
    cnt = 0
    for i in range(len(R)):
        if R[i] == v:
            cnt += 1
    print(cnt)
countv()
