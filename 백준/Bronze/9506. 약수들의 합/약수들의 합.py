def baek9506():
    while True:
        n = int(input())
        if n == -1:
            break
        arr = []
        for i in range(1, n):
            if n % i == 0:
                arr.append(i)
        if sum(arr) == n:
            print(f'{n} =', end=' ')
            for i in arr:
                if i == arr[-1]:
                    print(f'{i}', end=' ')
                else:
                    print(f'{i} +', end=' ')
        else:
            print(f'{n} is NOT perfect.')
baek9506()