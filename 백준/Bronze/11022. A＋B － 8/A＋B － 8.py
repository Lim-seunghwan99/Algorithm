def fastAB():
    import sys
    T = int(sys.stdin.readline().rstrip())
    for i in range(T):
        a, b = map(int,sys.stdin.readline().rstrip().split())
        res = a+b
        print(f'Case #{i+1}: {a} + {b} = {res}')
fastAB()