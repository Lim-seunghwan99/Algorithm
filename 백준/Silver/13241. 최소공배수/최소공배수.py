a, b = map(int, input().split())
if a > b:
    mx = a
    mn = b
else:
    mx = b
    mn = a
j = 1
res = 0
while True:
    if mx * j % mn == 0:
        res = mx * j
        break
    j += 1
print(res)