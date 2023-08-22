N, M = map(int, input().split())
a = [input() for _ in range(N)]  # 포함되어 있는 문자열
b = [input() for _ in range(M)]  # 검사해야 하는 문자열
cnt = 0
for i in range(M):
    if b[i] in a:
        cnt += 1
print(cnt)