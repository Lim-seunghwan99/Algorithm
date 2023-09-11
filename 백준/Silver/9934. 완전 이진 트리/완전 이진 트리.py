def inorder_traverse(n):
    global i
    if n * 2 <= len(arr):
        inorder_traverse(n*2)
    s1[n] = arr[i]
    i += 1
    if n * 2 + 1 <= len(arr):
        inorder_traverse(n * 2 + 1)


# 중위 순회
K = int(input())
arr = list(map(int, input().split()))
s1 = [0] * (len(arr)+1)
i = 0
inorder_traverse(1)
degree = 0
start = 1
while degree < K:
    end = start + 2 ** degree
    for i in range(start, end):
        print(s1[i], end=' ')
    print()
    degree += 1
    start = end
