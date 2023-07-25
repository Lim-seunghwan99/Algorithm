def alarm():
    H, M = list(map(int, input().split()))
    if (M - 45) < 0:
        if H == 0:
            H += 23
            M = M+60-45
            print(H, M)
        else:
            H -= 1
            M = M+60-45
            print(H, M)
    else:
        print(H, M-45)


alarm()