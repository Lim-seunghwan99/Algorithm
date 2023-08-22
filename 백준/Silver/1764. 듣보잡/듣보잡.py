import sys
N, M = map(int, sys.stdin.readline().split())
a = set([sys.stdin.readline().strip() for _ in range(N)])
b = set([sys.stdin.readline().strip() for _ in range(M)])
r = sorted(a & b)
s = len(r)
print(s)
for i in range(s):
    print(r[i])