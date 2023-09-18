import sys
sys.setrecursionlimit(10**5)
def express_set():
    n, m = list(map(int, input().split()))
    ex_set = [i for i in range(n+1)]  # 자기 자신을 부모 노드로 설정

    def find(a):
        if a == ex_set[a]:
            return a
        p = find(ex_set[a])
        ex_set[a] = p
        return ex_set[a]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b:
            return
        if a < b:
            ex_set[b] = a
        else:
            ex_set[a] = b

    for i in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            union(a, b)
        elif c == 1:
            if find(a) == find(b):
                print('YES')
            else:
                print('NO')
        #     if ex_set[a]:
        #         temp = idx[a]
        #         while ex_set[a] != temp:  # 루트 노드를 찾을 때 까지
        #             temp = ex_set[a]
        #         ex_set[a] = temp
        #         ex_set[b] = temp
        #     else:
        #         ex_set[a] = a
        #         ex_set[b] = a
        # elif c == 1:
        #     # print(f'ex_set: {ex_set}')
        #     # print(f'idx: {idx}')
        #     temp_a = idx[a]
        #     while ex_set[a] != temp_a:
        #         temp_a = ex_set[a]
        #     ans_a = temp_a
        #     temp_b = idx[b]
        #     while ex_set[b] != temp_b:
        #         temp_b = ex_set[b]
        #     ans_b = temp_b
        #     if ans_a == ans_b:
        #         print('YES')
        #     else:
        #         print('NO')


express_set()
