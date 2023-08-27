def find(cur):
    if len(s) == m:
        print(*s)
        return

    for i in range(cur-1, n+1):
        s.append(i)
        find(i+1)
        s.pop()


n, m = map(int, input().split())
arr = [i for i in range(n)]
s = []
find(2)