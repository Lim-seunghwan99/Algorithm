def professor():
    num = [i for i in range(1, 31)]
    mz = []
    for i in range(28):
        gb = int(input())
        if gb in num:
            num.remove(gb)
    sorted(num)
    print(num[0])
    print(num[1])

professor()