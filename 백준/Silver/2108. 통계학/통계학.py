N = int(input())
arr = []
dic = {}
for i in range(N):
    s = int(input())
    arr.append(s)
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
sv = sum(arr)
print(int(round(sv/N, 0)))
a1 = sorted(arr)
print(a1[N//2])
d2 = sorted(dic.items(), key=lambda x: x[1])
res = []
mx = d2[-1][-1]  # 벨류값의 최대 값
for i in range(len(d2)):
    if d2[i][1] == mx:
        res.append(d2[i][0])
res.sort()
if len(res) >= 2:
    print(res[1])
else:
    print(res[0])
print(max(arr)-min(arr))