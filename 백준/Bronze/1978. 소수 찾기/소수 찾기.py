def findprime2():
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        a = 0
        j = 1
        while j <= arr[i]:
            if arr[i] % j == 0:
                a += 1
            j += 1
        if a == 2:
            cnt += 1
    print(cnt)
findprime2()