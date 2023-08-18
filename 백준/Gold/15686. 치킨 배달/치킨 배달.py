N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chi = []
hou = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chi.append([i, j])
        elif arr[i][j] == 1:
            hou.append(([i, j]))
#print(chi)
#print(f'hou: {hou}')
# 치킨집 리스트에서 부분집합으로 M개를 뽑는다.
# M개의 치킨집에서 집 리스트와의 치킨 거리를 구하고, M개중 최솟값을
# 도시의 치킨 거리에 ++한다.
# M개의 부분집합 만큼 도시의 치킨 거리 모음리스트에 넣고, 그 중 최솟값을 출력한다.
# def ccc(i, M):
#     if i == M:
#         print(ccc)
#     for j in range(i, M+1):
#         chi[i], chi[j] = chi[j], chi[i]
#         ccc(i+1, M)
#         chi[i], chi[j] = chi[j], chi[i]
# ccc(0, M)

### 크기가 M인 부분집합 gpt 썼음
def generate_subsets(nums, M):
    def backtrack(start, subset):
        if len(subset) == M:
            subsets.append(subset[:])  # 새로운 부분집합 추가
            return
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

    subsets = []
    backtrack(0, [])
    return subsets


#original_list = [1, 2, 3, 4]  # 예시 리스트
# M = 3  # 부분집합의 길이
subsets = generate_subsets(chi, M)
#print(f'부분집합 : {subsets}')
#print(f'부분집합 길이: {len(subsets)}')
res = []
while subsets:
    t = subsets.pop(0)
    res3 = []
    for i in range(len(hou)):
        res2 = []
        for j in range(len(t)):
            sv = 0
            sv += abs(hou[i][0] - t[j][0])
            sv += abs(hou[i][1] - t[j][1])
            res2.append(sv)
        res3.append(min(res2))
    res.append(sum(res3))
print(min(res))