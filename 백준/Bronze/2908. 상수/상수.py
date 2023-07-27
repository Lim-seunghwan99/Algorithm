def mathstudy():
    a, b = list(map(str, input().split()))
    n_a = a[::-1]
    n_b = b[::-1]
    if int(n_a) > int(n_b):
        return n_a
    else:
        return n_b


print(mathstudy())