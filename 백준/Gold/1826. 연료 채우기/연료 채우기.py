N = int(input())
arr = [[]]
for i in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
arr.sort()
vlg = [0] * N
oil = [0] * N
for j in range(1, N+1):
    vlg[j-1] = arr[j][0]
    oil[j-1] = arr[j][1]
p, l = map(int, input().split())
vlg.append(p)  # 여기까지 오름차순으로 마을거리, 오일을 정렬하고 1차원 배열에 담았음
cur = l  # 시작 기름
i = 0  # 움직이는 범위
oil_lst = []
res = 0
while True:
    if cur >= vlg[-1]:
        break
    if cur >= vlg[i]:
        oil_lst.append(oil[i])
        i += 1
        continue
    else:
        if oil_lst:
            while oil_lst:
                if cur >= vlg[i]:
                    break
                else:
                    oil_lst.sort()  # 정렬해서
                    cur += oil_lst.pop()  # 최댓값을 뽑아서 더한다.
                    res += 1
        else:
            res = -1
            break
print(res)