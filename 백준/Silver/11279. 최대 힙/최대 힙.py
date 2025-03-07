import heapq
import sys
input = sys.stdin.readline
N = int(input())
hq = []
for i in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(hq, -x)
    else:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)



