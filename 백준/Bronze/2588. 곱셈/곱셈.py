a = int(input())
b = list(map(int, input()))

sv = 0
for i in range(len(b)):
    sv += (b[2-i] * a * 10 ** i)
    print(b[2-i] * a)
print(sv)