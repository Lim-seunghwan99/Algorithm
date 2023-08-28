N = int(input())
arr = []
for i in range(N):
    w = int(input())  #
    arr.append(w)
arr.sort()
sv = 0
mx = 0
for i in range(N):
    sv = arr[i] * (N - i)
    mx = max(sv, mx)
print(mx)