def fibo(n):
    global memo
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo(n-1) + fibo(n-2) * 2
        return memo[n]
n = int(input())
memo = [0] * (n + 2)
memo[1] = 1
memo[2] = 3
res = fibo(n) % 10007
print(res)