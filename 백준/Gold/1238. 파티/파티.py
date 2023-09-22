import heapq
n, m, t = map(int, input().split())
# n번 까지의 집, m개의 간선, t목표 지점
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y, c = map(int, input().split())
    graph[x].append([y, c])


# print(graph)

# 누적 거리 저장
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


ans = [0] * (n + 1)
for i in range(1, n + 1):
    distance = [float('inf')] * (n + 1)
    dijkstra(i)
    # print(f'{i} {distance[t]}')
    if i == t:
        # print('여기 찍힘')
        for j in range(1, n + 1):
            temp = distance[j]
            ans[j] += temp
    else:
        temp = distance[t]
        ans[i] += temp
        # print('여기 찍힘2')
    # print(f'{i} {distance}')
print(f'{max(ans)}')