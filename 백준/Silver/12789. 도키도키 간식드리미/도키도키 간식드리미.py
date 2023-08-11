def snack():
    import sys
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    stack = []
    num = 1
    res = []
    while arr:
        if stack and stack[-1] == num:
            res.append(stack.pop())
            num += 1
        elif arr[0] != num:
            stack.append(arr.pop(0))
        elif arr[0] == num:
            res.append(arr.pop(0))
            num += 1
    while stack:
        res.append(stack.pop())
    if res == [i for i in range(1, N+1)]:
        print('Nice')
    else:
        print('Sad')

snack()