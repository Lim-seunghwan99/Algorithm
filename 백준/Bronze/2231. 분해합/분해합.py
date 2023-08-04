def baek2231():
    N = int(input())
    sv = 0
    res = []
    for i in range(N+1):
        num = i
        sv = 0
        sv += i
        while i != 0:
            sv += i % 10 #
            i = i // 10
        if sv == N:
            res.append(num)
    if len(res) == 0:
        print(0)
    else:
        print(min(res))
baek2231()