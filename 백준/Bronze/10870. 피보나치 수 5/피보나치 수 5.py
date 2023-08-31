def f(i):
    if i < 2:
        return memo[i]
    else:
        if memo[i] == 0:
            memo[i] = f(i-1) + f(i-2)
        return memo[i]


N = int(input())
memo = [0] * (N+2)
memo[0] = 0
memo[1] = 1
print(f(N))