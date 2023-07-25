def fastAB():
    import sys
    while True:
    #T = int(sys.stdin.readline().rstrip())
    #for i in range(T):
        a, b = map(int,sys.stdin.readline().rstrip().split())
        if a == 0 and b == 0:
            break
        res = a+b
    #print(f'Case #{i+1}: {a} + {b} = {res}')
        print(res)
fastAB()