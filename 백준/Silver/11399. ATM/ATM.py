def atm():
    N = int(input())
    P = list(map(int, input().split()))
    # i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분
    # 인출하는데 걸리는 시간을 최솟값으로 정렬해서 합하면서 간다.
    P.sort()
    #print(P)
    sv = 0
    mx_sv =0
    for i in range(N):
        sv += P[i]
        mx_sv += sv
        # 1 + 3 + 6 + 9 + 13 = 32
    print(mx_sv)
    # print(sv)


atm()