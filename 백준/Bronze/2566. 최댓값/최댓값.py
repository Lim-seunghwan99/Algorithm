def ret():
    import pprint
    a = list(list(map(int, input().split())) for _ in range(9))
    mn = 0
    mc = 0
    mr = 0
    for row in range(9):
        for col in range(9):
            if mn <= a[row][col]:
                mr = row + 1
                mc = col + 1
                mn = a[row][col]
    print(mn)
    print(mr, mc)

ret()