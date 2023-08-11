def top():
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    res = [0] * N

    for i, num in enumerate(arr):
        while stack and stack[-1][1] <= num: # num보다 한단계 큰 값을 찾을 때 까지 계속 pop
            stack.pop()

        if stack: # 스택이 있으면 레이저가 걸린다는 뜻
            res[i] = stack[-1][0] # 스택의 가장 큰 값의 인덱스를 반환

        stack.append((i + 1, num)) # 스택에 계속 넣는다 내림차순으로 비교하기 위해서

    print(*res, sep=' ')

top()