N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr += arr[:k-1]

lft, rgt = 0, k
result = 0
dict = {}
# 쿠폰을 가지고 갈 경우
dict[c] = 1
# 처음 범위 설정
for i in range(k):
    if arr[i] in dict:
        dict[arr[i]] += 1
    else:
        dict[arr[i]] = 1

for x in range(k, N + k - 1):
    dict[arr[lft]] -= 1
    if arr[rgt] in dict:
        dict[arr[rgt]] += 1
    else:
        dict[arr[rgt]] = 1
    if dict[arr[lft]] == 0:
        dict.pop(arr[lft])
    lft += 1
    rgt += 1
    result = max(result, len(dict))

print(result)