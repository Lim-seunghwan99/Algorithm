N = int(input())
dic = {}
for i in range(N):
    a, b = input().split()
    if a == 'ChongChong' or b == 'ChongChong':
        dic[a] = 1
        dic[b] = 1
        continue
    elif a in dic or b in dic:
        dic[a] = 1
        dic[b] = 1
print(len(dic))