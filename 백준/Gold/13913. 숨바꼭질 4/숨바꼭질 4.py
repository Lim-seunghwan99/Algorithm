def boj13913():
    import sys
    from collections import deque
    input = sys.stdin.readline
    # 1초 후에 X - 1, X + 1, 2 * X로 이동 가능
    N, K = list(map(int, input().split()))
    visited = [-1] * 100001
    prev = [-1] * 100001
    q = deque()
    q.append(N)
    visited[N] = 0
    while q:
        cur = q.popleft()
        if cur == K:
            break
        for nxt in (cur - 1, cur + 1, cur * 2):
            if 0 <= nxt <= 100000 and visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                prev[nxt] = cur
                q.append(nxt)

    print(visited[K])
    ans_lst = []
    cur = K
    while cur != -1:
        ans_lst.append(cur)
        cur = prev[cur]
    ans_lst.reverse()

    print(*ans_lst)



if __name__ == "__main__":
    boj13913()