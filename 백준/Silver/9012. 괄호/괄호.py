def check():
    T = int(input())
    for tc in range(1, T + 1):
        arr = list(map(str, input()))
        chk = ['(', '{', '[']
        chk2 = [')', '}', ']']
        a = []
        for c in range(len(arr)):
            if arr[c] in chk:
                a.append(arr[c])
            elif arr[c] in chk2:
                if len(a) == 0:
                    a.append(1)
                    break
                if a.pop(-1) == chk[chk2.index(arr[c])]:
                    continue
                else:
                    a.append(1)
                    break
        if len(a) > 0:
            res = 'NO'
        else:
            res = 'YES'
        print(res)

check()