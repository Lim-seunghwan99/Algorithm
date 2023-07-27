def studywords():
    words = input()
    words = words.upper()
    k = [0] * 26
    mx = 0
    mx2 = 0
    for i in words:
        k[ord(i)-65] += 1
    for j in range(len(k)):

        if k[j] > mx:
            mx = k[j]
            mx_i = k.index(k[j])
        elif k[j] == mx:
            mx2 = k[j]
        else:
            continue
    if mx == mx2:
        print('?')
    else:
        print(chr(mx_i+65))

studywords()