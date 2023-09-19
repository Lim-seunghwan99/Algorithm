N = int(input())
M = int(input())
# 유니온 파인드를 이용해서 조상이 같은지 확인하는 문제다
parents = [i for i in range(N+1)]
def find(x):
    if x == parents[x]:  # 만약 루트 노드면 멈춰라
        return x
    p = find(parents[x])  # 아닐 경우 부모노드를 이용해서 다시 find
    parents[x] = p  # 현 위치에는 부모노드를 입력한다.
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
for i in range(1, N+1):
    arr = [0] + list(map(int, input().split()))
    for j in range(1, N):
        if arr[j] == 1:
            union(i, j)
chk = list(map(int, input().split()))
ans = 'YES'
temp = find(chk[0])
for i in range(1, len(chk)):
    if temp != find(chk[i]):
        ans = 'NO'
        break
#print(parents)
print(ans)