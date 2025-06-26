import sys
input = sys.stdin.readline
import heapq


def boj11779():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        s, e, w = list(map(int, input().split()))
        graph[s].append((w, e))
    visited = [float('inf')] * (n + 1)
    m_start,m_end = list(map(int, input().split()))
    # 출발 도시에서 도착 도시까지 가는데 드는 최소비용
    # 최소비용을 갖는 경로에 포함되어있는 도시의 개수 출력, 출발 도시, 도착 도시 포함
    # 최소비용을 갖는 경로를 방문하는 도시 순서대로 출력
    m_hist = [m_start]
    def dijkstra(start, end, hist):
        hp = []
        heapq.heappush(hp, (0, start, hist))
        visited[start] = 0
        ans_hist = []
        while hp:
            acc_cost, now, hist = heapq.heappop(hp)


            if visited[now] < acc_cost:
                continue

            if end == now:
                ans_hist = hist[:]

            for cost, nxt in graph[now]:
                new_cost = acc_cost + cost

                if new_cost < visited[nxt]:
                    visited[nxt] = new_cost
                    hist.append(nxt)
                    temp = hist[:]
                    heapq.heappush(hp, (new_cost, nxt, temp))
                    hist.pop()
        return ans_hist


    m_hist = dijkstra(m_start, m_end, m_hist)
    print(visited[m_end])
    print(len(m_hist))
    print(*m_hist)






if __name__ == "__main__":
    boj11779()