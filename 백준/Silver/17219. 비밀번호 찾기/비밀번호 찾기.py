import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for _ in range(N):
    x, y = input().split()
    dic[x] = y

for _ in range(M):
    print(dic[input().strip()])
