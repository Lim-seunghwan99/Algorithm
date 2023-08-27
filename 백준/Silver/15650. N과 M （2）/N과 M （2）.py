def find(cur):
    if len(s) == M:
        print(*s)
        return
    for i in range(cur, N+1):
        if i not in s:
            s.append(i)
            find(i+1)
            s.pop()
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
s = []
find(1)