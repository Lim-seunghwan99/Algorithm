def alpha():
    t = int(input())
    for _ in range(t):
        a = input()
        print(''.join(a[0]+a[-1]))
alpha()