N = int(input())
dic = {}
cnt = 0
for i in range(N):
    word = input()
    if word == 'ENTER':
        dic = {}
        continue
    elif word in dic:
        continue
    dic[word] = 1
    cnt += 1
print(cnt)