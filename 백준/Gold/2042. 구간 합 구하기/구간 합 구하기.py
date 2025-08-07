N, M, K = list(map(int, input().split()))
arr = [0] * (N + 1)
tree = [0] * (4 * N)

for i in range(1, N + 1):
    arr[i] = int(input())


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, diff)
    update(mid + 1, end, node * 2 + 1, index, diff)


def query(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)


init(1, N, 1)

for i in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(1, N, 1, b, diff)
    else:
        print(query(1, N, 1, b, c))
