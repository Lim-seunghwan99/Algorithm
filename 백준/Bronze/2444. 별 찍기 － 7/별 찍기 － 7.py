def countingstars7():
    n = int(input())
    for i in range(n+1):
        if i < n:
            print(' '*(n - 1 - i)+'*' * (2 * i + 1))
        else:# i = 5 i =5, n=5
            for j in range(n-1): #range(4), j=0
                print(' '*(j + 1)+'*' * ((2 * n - 1)-(2 * (j+1))))

countingstars7()