def f(b, sv, cnt):
    global mi
    global res
    cnt += 1
    if sv > b:
        return
    if sv == b:
        if mi > cnt:
            mi = cnt
            res.append(mi)
    else:
        sv1 = sv * 2
        f(b, sv1, cnt)
        sv2 = (sv * 10)+1
        f(b, sv2, cnt)


# A를 B로 바꾸려고 한다.
# 가능한 연산은
# *2
# *10 +1
# 두가지 이다.
a, b = map(int, input().split())
cnt = 0
mi = 1000000001
res = []
f(b, a, 0)
if res:
    print(min(res))
else:
    print(-1)