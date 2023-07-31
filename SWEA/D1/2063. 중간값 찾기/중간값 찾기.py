N = int(input())
a = list(map(int, input().split()))
a.sort()
c = N//2
result = a[c]
print(result)