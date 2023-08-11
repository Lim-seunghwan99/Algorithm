def top():
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    res = [0] * N

    for i, num in enumerate(arr):
        while stack and stack[-1][1] <= num:
            stack.pop()

        if stack:
            res[i] = stack[-1][0]

        stack.append((i + 1, num))

    print(*res, sep=' ')

top()