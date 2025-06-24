import sys
input = sys.stdin.readline
import heapq


def boj1753():
    V, E = list(map(int, input().split()))
    K = int(input())  # 시작 점
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        u,v,w = list(map(int, input().split()))
        graph[u].append((v, w))

    distance = [float('inf')] * (V + 1)
    # K 번과의
    def dijkstra(start):
        pq = []
        heapq.heappush(pq, (0, start))
        distance[start] = 0

        while pq:
            dist, now = heapq.heappop(pq)

            if distance[now] < dist:
                continue

            for nxt_node, cost in graph[now]:
                new_cost = dist + cost

                if new_cost < distance[nxt_node]:
                    distance[nxt_node] = new_cost
                    heapq.heappush(pq, (new_cost, nxt_node))

    dijkstra(K)
    for i in range(1, len(distance)):
        if distance[i] == float('inf'):
            print("INF")
        else:
            print(distance[i])






if __name__ == "__main__":
    boj1753()