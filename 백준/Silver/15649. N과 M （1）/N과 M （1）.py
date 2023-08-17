def baektracking():
    if len(num) == M:
        print(' '.join(map(str, num)))
        return

    for i in range(1, N+1):
        if i not in num:
            num.append(i)
            baektracking()
            num.pop()

N, M = list(map(int, input().split()))
num = []
baektracking()