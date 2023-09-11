import sys
M = int(sys.stdin.readline())
A = []
sv = 0
xor = 0
for i in range(M):
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 1:
        sv += arr[1]
        xor = xor ^ arr[1]
    elif arr[0] == 2:
        sv -= arr[1]
        xor = xor^arr[1]
    elif arr[0] == 3:
        print(sv)
    else:
        print(xor)