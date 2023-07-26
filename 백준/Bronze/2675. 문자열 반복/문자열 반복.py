def string():
    t = int(input())

    for i in range(t):
        r, s = input().split()
        p = []
        for o in range(len(s)):
            p.append(s[o] * int(r))
        print(''.join(p))
string()