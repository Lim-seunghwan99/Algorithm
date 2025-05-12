def boj1240():
    N, M = list(map(int, input().split()))
    # 트리 상에 연결된 두 점과 거리를 입력받는다.
    tree = [[] for _ in range(N + 1)]
    from collections import deque
    def bfs(lst, ans):
        res = 0
        while lst:
            node, wgt = lst.popleft()  # 2, 2
            if node == ans:
                return res + wgt
            else:
                for nxt in range(len(tree[node])):
                    if not visited[tree[node][nxt][0]]:
                        tmp = tree[node][nxt][1] + wgt
                        lst.append([tree[node][nxt][0], tmp])
                        visited[tree[node][nxt][0]] = True



    for _ in range(N - 1):
        start, end, weight = list(map(int, input().split()))
        tree[start].append([end, weight])
        tree[end].append([start, weight])
    for _ in range(M):
        chk1, chk2 = list(map(int, input().split()))
        visited = [False] * len(tree)
        q = deque()
        for t in range(len(tree[chk1])):
            visited[chk1] = True
            q.append(tree[chk1][t])
        print(bfs(q, chk2))





if __name__ == "__main__":
    boj1240()