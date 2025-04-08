def boj13549():
    from collections import deque
    N, K = list(map(int, input().split()))
    # 걷거나 순간 이동
    time = 0
    visited = [10**9] * (100000 + 1)
    # 해당 위치에 방문했을 떄 최솟값이 중요한거 아닌가?
    q = deque()
    visited[N] = 0
    if N - 1 >= 0:
        q.append([N - 1, time + 1])  # X+1로 이동
        visited[N - 1] = time + 1
    if N + 1 <= 100000:
        q.append([N + 1, time + 1])  # X+1로 이동
        visited[N + 1] = time + 1
    if 2 * N <= 100000 and visited[N * 2] > time:  # 시간이 더 적으면
        q.append([N * 2, time])  # 2배 순간 이동
        visited[N * 2] = time

    while q:
        cur, time = q.popleft()
        if cur == K:
            break
        if cur * 2 <= 100000 and visited[cur * 2] > time:
            q.append([cur * 2, time])  # 2배 순간 이동
            visited[cur * 2] = time
        if cur + 1 <= 100000 and visited[cur + 1] > time + 1:
            q.append([cur + 1, time + 1])  # X+1로 이동
            visited[cur + 1] = time + 1
        if cur - 1 >= 0 and visited[cur - 1] > time + 1:
            q.append([cur - 1, time + 1])  # X-1로 이동
            visited[cur - 1] = time + 1

    print(visited[K])


if __name__ == "__main__":
    # boj15665()
    # boj16987()
    # boj5427()
    boj13549()