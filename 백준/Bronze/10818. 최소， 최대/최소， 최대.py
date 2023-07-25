N = int(input())
T = list(map(int, input().split()))
max_n = T[0]
min_n = T[0]
for i in range(N):
    if T[i] > max_n:
        max_n = T[i]
    elif T[i] < min_n:
        min_n = T[i]
print(f'{min_n} {max_n}')