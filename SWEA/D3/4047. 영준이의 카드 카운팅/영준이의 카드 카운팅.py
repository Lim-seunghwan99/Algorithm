T = int(input())
for tc in range(1, T+1):
    arr = input()
    S = [0] * 13
    D = [0] * 13
    H = [0] * 13
    C = [0] * 13
    res = ''
    for i in range(0, len(arr), 3):
        if arr[i] == 'S':
            num = int(arr[i+1]+arr[i+2])
            if S[num-1] == 0:
                S[num-1] = 1
            else:
                res = 'ERROR'
                break
        elif arr[i] == 'D':
            num = int(arr[i + 1] + arr[i + 2])
            if D[num-1] == 0:
                D[num-1] = 1
            else:
                res = 'ERROR'
                break
        elif arr[i] == 'H':
            num = int(arr[i+1]+arr[i+2])
            if H[num-1] == 0:
                H[num-1] = 1
            else:
                res = 'ERROR'
                break
        elif arr[i] == 'C':
            num = int(arr[i+1]+arr[i+2])
            if C[num-1] == 0:
                C[num-1] = 1
            else:
                res = 'ERROR'
                break

    if res == 'ERROR':
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} {S.count(0)} {D.count(0)} {H.count(0)} {C.count(0)}')