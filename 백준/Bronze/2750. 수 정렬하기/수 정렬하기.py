T = int(input())
n = []
for i in range(T):
    n += (list(map(int, input().split())))
    n.sort()
print('\n'.join(map(str, n)))