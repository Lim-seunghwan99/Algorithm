# 하노이의 탑
n = int(input())
# 한칸씩 밖에 못 옮긴다. 1번에 있으면 2번에 다 옮기고 3번에 한칸 쌓고
# 다시 다 옮기고 3번에 한칸 쌓는 형태
cnt = 0
res = []
def f(N, s, a1, a2):
    global cnt
    cnt += 1
    if N == 1:
        res.append([s, a1])
    else:
        f(N-1, s, a2, a1)
        res.append([s, a1])
        f(N-1, a2, a1, s)

f(n, 1, 3, 2)
print(cnt)
for i in range(cnt):
    print(*res[i])