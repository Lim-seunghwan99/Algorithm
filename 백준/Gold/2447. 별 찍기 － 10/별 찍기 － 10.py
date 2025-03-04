# N은 3의 거듭제곱으로 주어진다
def p(N):
    if N == 1:
        return ['*']
    
    stars = p(N//3)
    L = []

    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s + ' '*(N//3) + s)
    for s in stars:
        L.append(s*3)
    return L

N = int(input())
print('\n'.join(p(N)))
p(N)