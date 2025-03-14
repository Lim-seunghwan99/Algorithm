from collections import deque

F, S, G, U, D = list(map(int, input().split()))
# 총 F층, S 시작점, G 도착점, U 위로 움직일 수 있는 충, D 아래로 움직일 수 있는 층
q = deque([[S, 0]])
visited = [False] * (F + 1)
visited[S] = True
ans = 0
while q:
    v = q.popleft()
    current, ans = v[0], v[1]
    if current == G:
        print(ans)
        break
    if current + U <= F and visited[current + U] is False:
        q.append([current + U, ans + 1])
        visited[current + U] = True
    if current - D > 0 and visited[current - D] is False:
        q.append([current - D, ans + 1])
        visited[current - D] = True
else:
    print("use the stairs")


