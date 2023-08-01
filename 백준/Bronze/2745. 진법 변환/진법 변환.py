def baek2745():
    n, k = input().split()
    res = []
    sv = 0
    for i in n:
        if 48 <= ord(i) <= 57:
            res.append(i)
        else:
            ch = ord(i) - 55
            res.append(ch)
    for j in range(0, len(res)):
        n_r = res.pop(-1)
        nn = (int(k) ** j)# k와 그 자리 의 배수
        sv += nn * int(n_r)  # operands do not support **
    print(sv)


baek2745()