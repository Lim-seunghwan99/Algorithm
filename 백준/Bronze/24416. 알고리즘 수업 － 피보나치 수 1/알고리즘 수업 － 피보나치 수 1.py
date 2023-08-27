def fib(n):
    global cnt
    if n < 2:
        return f[n]
    else:
        if f[n] == 0:
            f[n] = fib(n-1) + fib(n-2)
            cnt += 1
        return f[n]
n = int(input())
f = [0] * (n + 1)
f[0] = 1
f[1] = 1
cnt = 0
print(fib(n-1), cnt)