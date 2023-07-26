def alpha():
    n = int(input())
    m = int(input())
    m = str(m)
    sv = 0
    for i in range(len(m)):
        sv += int(m[i])
    return sv
print(alpha())