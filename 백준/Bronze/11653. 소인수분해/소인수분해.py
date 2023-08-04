def primen():
    N = int(input())
    if N == 1:
        print()
    j = 2
    while 1 < N:
        if N % j == 0:
            print(j)
            N /= j
        else:
            j += 1

primen()