def gasstation():
    N = int(input())
    arr = list(map(int, input().split())) # 도로의 길이 키로당 1리터
    pr = list(map(int, input().split())) # 리터당 가격
    sv = 0
    cur = 0
    walk = 0
    i = 0
    while cur < N-1:
        if pr[cur+i] >= pr[cur+1+i]:
            walk += arr[cur+i]
            sv += walk * pr[cur]
            cur += i + 1
            i = 0
            walk = 0
        else:
            walk += arr[cur]
            i += 1
    print(sv)


gasstation()