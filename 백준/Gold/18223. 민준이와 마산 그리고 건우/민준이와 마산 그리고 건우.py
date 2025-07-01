import sys
input = sys.stdin.readline
import heapq


def boj18223():

    V, E, P = list(map(int, input().split()))  # 정점의 개수, 간선의 개수, 건우가 위치한 정점
    visited = [float('inf')] * (V + 1)
    visited2 = [float('inf')] * (V + 1)
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b, c = list(map(int, input().split()))
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start, visited):
        hp = []
        heapq.heappush(hp, (0, start))
        visited[1] = 0
        while hp:
            acc_cost, now = heapq.heappop(hp)

            if visited[now] < acc_cost:
                continue


            for nxt, cost in graph[now]:
                new_cost = acc_cost + cost

                if new_cost < visited[nxt]:
                    visited[nxt] = new_cost
                    heapq.heappush(hp, (new_cost, nxt))

    dijkstra(1, visited)
    dijkstra(P, visited2)
    if visited[V] == visited2[V] + visited[P]:
        print("SAVE HIM")
    else:
        print("GOOD BYE")


if __name__ == "__main__":
    boj18223()