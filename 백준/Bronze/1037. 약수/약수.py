a = int(input())
arr = list(map(int, input().split()))
sv = 0
if len(arr) <= 1:
    sv = arr[0] ** 2
else:
    sv = max(arr) * min(arr)
print(sv)