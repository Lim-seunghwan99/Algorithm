s = list(input())
t = list(input())
ans = 0
while len(s) < len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]

if s == t:
    ans = 1
print(ans)