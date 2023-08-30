N, M = map(int, input().split())
d = {}
for i in range(N):
    s = input()
    if len(s) < M:
        continue
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
d2 = sorted(d.items(), key=lambda x: (-x[-1], -len(x[0]), x[0]))
# sorted에서 람다함수를 통해서 다중 조건을 걸 수 있다.
for i in d2:
    print(i[0])