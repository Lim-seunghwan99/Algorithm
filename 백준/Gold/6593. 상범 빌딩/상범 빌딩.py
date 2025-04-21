def boj6593():
    from collections import deque
    dx = [0, 1, 0, -1, 0, 0]
    dy = [1, 0, -1, 0, 0, 0]
    dk = [0, 0, 0, 0, 1, -1] # 0은 같은 층, 1은 위층, -1은 아래층

    def bfs(k, r, s):
        q = deque()
        q.append((k, r, s))
        while q:
            z, y, x = q.popleft()
            for floor in range(6):
                nz = z + dk[floor]
                ny = y + dy[floor]
                nx = x + dx[floor]
                if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C and visited[nz][ny][nx] == 0:
                    if arr[nz][ny][nx] == ".":
                        visited[nz][ny][nx] = visited[z][y][x] + 1
                        q.append((nz, ny, nx))
                    if arr[nz][ny][nx] == "E":
                        return visited[z][y][x] + 1

        else:
            return False

    while True:
        L, R, C = list(map(int, input().split()))
        if L == R == C == 0:
            break
        # R, C는 각 층의 행과 열 개수, L은 층 수
        # #은 금으로 막혀있는 칸, . 은 비어있는 칸,
        # 각 층 사이에는 빈 줄이 있다. 층 간에 빈줄이 있으면 내려갈 수 있음
        arr = []
        for case in range(L):
            arr.append(list(input() for _ in range(R)))
            if case != L - 1:
                input()
        visited = [[[0] * C for _ in range(R)] for _ in range(L)]
        for k in range(L):
            for r in range(R):
                for c in range(C):
                    if arr[k][r][c] == "S":
                        chk = bfs(k, r, c)
                        if chk > 0:
                            print(f"Escaped in {chk} minute(s).")
                        else:
                            print("Trapped!")
        # 줄바꿈
        input()


if __name__ == "__main__":
    boj6593()