a, b = map(int, input().split())
c = int(input())

minute = a * 60 + b + c
if minute//60 >= 24:
    a = (minute//60)-24
else:
    a = minute // 60
b = minute % 60
print(a, b)