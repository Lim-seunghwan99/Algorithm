def costco():
    X = int(input())
    N = int(input())
    sv = 0
    for i in range(N):
        a, b = list(map(int, input().split()))
        sv += (a*b)
    if sv == X:
        print('Yes')
    else:
        print('No')
costco()