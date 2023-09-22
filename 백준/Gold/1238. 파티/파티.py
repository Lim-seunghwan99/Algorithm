def boj1238():
    import heapq
    
    def dijkstra(start, dist, graph, distance):
        h = []
        heapq.heappush(h, (dist, start))
        distance[start] = dist
        while h:
            dist, node = heapq.heappop(h)
            for nxt in graph[node]:
                nxt_node = nxt[0]
                nxt_dist = nxt[1]
                if distance[nxt_node] > dist + nxt_dist:
                    distance[nxt_node] = dist + nxt_dist
                    heapq.heappush(h, (distance[nxt_node], nxt_node))

    n, m, x = map(int, input().split())
    graph1 = [[] for _ in range(n + 1)]
    graph2 = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph1[s].append((e, t))
        graph2[e].append((s, t))
    distance1 = [float('inf')] * (n+1)
    dijkstra(x, 0, graph1, distance1)

    distance2 = [float('inf')] * (n + 1)
    dijkstra(x, 0, graph2, distance2)

    ans = 0
    for i in range(1, n+1):
        ans = max(ans, distance1[i] + distance2[i])
    print(ans)


boj1238()