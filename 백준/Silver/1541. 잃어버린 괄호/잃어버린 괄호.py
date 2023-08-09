def baek1541():
    arr = input().split('-')
    sv = 0
    for i in range(len(arr)):
        if i == 0:
            if '+' in arr[i]:
                k = arr[i].split('+')
                sv_l = [int(k[i]) for i in range(len(k))]
                de = sum(sv_l)
                sv += de
            else:
                sv += int(arr[i])
        if i > 0:
            if '+' in arr[i]:
                k = arr[i].split('+')
                sv_l = [int(k[i]) for i in range(len(k))]
                de = sum(sv_l)
                sv -= de
            else:
                sv -= int(arr[i])
    print(sv)

baek1541()