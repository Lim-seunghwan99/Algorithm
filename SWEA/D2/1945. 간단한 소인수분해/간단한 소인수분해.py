def Factorization():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        cnt_a = 0
        while N % 2 == 0:
            N = N / 2
            cnt_a += 1
        cnt_b = 0
        while N % 3 == 0:
            N = N / 3
            cnt_b += 1
        cnt_c = 0
        while N % 5 == 0:
            N = N / 5
            cnt_c += 1
        cnt_d = 0
        while N % 7 == 0:
            N = N / 7
            cnt_d += 1
        cnt_e = 0
        while N % 11 == 0:
            N = N / 11
            cnt_e += 1
        print(f'#{tc} {cnt_a} {cnt_b} {cnt_c} {cnt_d} {cnt_e}')
 
Factorization()