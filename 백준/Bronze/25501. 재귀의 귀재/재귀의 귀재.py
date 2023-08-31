def rec(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return rec(s, l+1, r-1)


def isPal(s):
    return rec(s, 0, len(s)-1)

T = int(input())
for i in range(T):
    cnt = 0
    s = input()
    print(isPal(s), cnt)