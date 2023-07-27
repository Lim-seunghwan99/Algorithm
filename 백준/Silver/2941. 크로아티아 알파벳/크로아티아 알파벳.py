def croatia():
    cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    n = input()

    for i in cro:
        n = n.replace(i, '*')
    print(len(n))


croatia()