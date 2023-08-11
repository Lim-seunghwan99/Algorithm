def stack2():
    import sys
    N = int(sys.stdin.readline())
    stack = []
    for i in range(N):
        num = sys.stdin.readline().split()
        if num[0] == '1':
            stack.append(int(num[1]))
        elif num[0] == '2':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif num[0] == '3':
            print(len(stack))
        elif num[0] == '4':
            if stack:
                print(0)
            else:
                print(1)
        elif num[0] == '5':
            if stack:
                print(stack[-1])
            else:
                print(-1)


stack2()