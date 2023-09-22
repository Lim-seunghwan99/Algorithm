def boj1504():
    # 임의로 주어진 두 정점은 반드시 통과해야한다.
    import heapq
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    u, v = map(int, input().split())

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


    ans1 = 0
    ans2 = 0
    if u and v:
        for i in range(N+1):
            if i == u:
                distance = [float('inf')] * (N + 1)
                dijkstra(1)
                ans1 += distance[i]
                # print(f'start:{i} ans1:{ans1} dist:{distance}')
                start2 = u
                start3 = v
                distance = [float('inf')] * (N + 1)
                dijkstra(start2)
                ans1 += distance[start3]
                # print(f'start2:{start2} ans1:{ans1} dist:{distance}')
                distance = [float('inf')] * (N + 1)
                dijkstra(start3)
                ans1 += distance[N]
                # print(f'start3:{start3} ans1:{ans1} dist:{distance}')

            elif i == v:
                distance = [float('inf')] * (N + 1)
                dijkstra(1)
                ans2 += distance[i]
                # print(f'start:{i} ans2:{ans2} dist:{distance}')
                start2 = v
                start3 = u
                distance = [float('inf')] * (N + 1)
                dijkstra(start2)
                ans2 += distance[start3]
                # print(f'start2:{start2} ans2:{ans2} dist:{distance}')
                distance = [float('inf')] * (N + 1)
                dijkstra(start3)
                ans2 += distance[N]
                # print(f'start3:{start3} ans2:{ans2} dist:{distance}')
        # print(ans1, ans2)
        ans = min(ans1, ans2)
        if ans == float('inf'):
            ans = -1
        print(ans)
    else:
        distance = [float('inf')] * (N + 1)
        dijkstra(1)
        ans = distance[N]
        if ans == float('inf'):
            ans = -1
        print(ans)


boj1504()