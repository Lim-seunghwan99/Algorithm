def fibo(n):
    global memo
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

num = int(input())
memo = [0] * (num + 2)
memo[1] = 1
memo[2] = 2
res = fibo(num) % 10007
print(res)