a, b = map(int, input().split())
c, d = map(int, input().split())
# b와 d의 최소공배수를 구해야 한다.
# 그 값을 b, d로 나누어 a, b에 곱해준다.
# 더 한후 최대 공약수를 찾아 그 값으로 나누어준다.
if b > d:
    mx = b
    mn = d
else:
    mn = b
    mx = d
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
g = gcd(mx, mn)
# g는 최대공약수이다.
# 최소공배수는 a, b를 곱한값을 최대공약수로 나누어 주면 된다.
cnt = mx * mn / g
x = cnt / d
y = cnt / b
aa = y * a
cc = x * c
#denominator = cnt
ddd = cnt
#numerator = aa + cc
nnn = aa + cc
k = gcd(nnn, ddd)
print(int(nnn / k),int(ddd / k))