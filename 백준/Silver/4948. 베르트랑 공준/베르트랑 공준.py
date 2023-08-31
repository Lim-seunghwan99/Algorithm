while True:
    N = int(input())
    if N == 0:
        break
    arr = [i for i in range(N)]
    prime = []
    for i in range(N+1, 2*N+1):
        if i == 1:
            continue
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime.append(i)
    print(len(prime))
