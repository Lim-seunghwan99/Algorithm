import sys
from collections import deque
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
idx = [i for i in range(N)]
q = deque(arr)
im = deque(idx)
while q:
    a = q.popleft()
    res = im.popleft()
    if a > 0:
        q.rotate(1 - a)
        im.rotate(1 - a)
    else:
        q.rotate(-a)
        im.rotate(-a)
    print(res+1, end=' ')