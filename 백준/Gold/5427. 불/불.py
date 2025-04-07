def boj5427():
    from collections import deque
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    T = int(input())
    for _ in range(T):
        w, h = list(map(int, input().split()))
        arr = [list(input()) for _ in range(h)]
        visited_fire = [[10**9] * w for _ in range(h)]
        visited_p = [[False] * w for _ in range(h)]
        # . 이 빈공간
        # # 이 벽
        # @ 상근이의 시작 위치
        # * 불, 불은 1초마다 번진다, 불리스트를 만들어서 1초마다 갱신?
        # visited랑, #이용
        def burn(fires):
            while fires:
                x, y = fires.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != "#":
                        new_time = visited_fire[x][y] + 1
                        if visited_fire[nx][ny] > new_time:
                            visited_fire[nx][ny] = new_time
                            fires.append((nx, ny))


        def person(start):
            p = deque()
            p.append(start)
            while p:
                x, y, cnt = p.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < h and 0 <= ny < w:
                        if visited_p[nx][ny] is False and arr[nx][ny] == "." and visited_fire[nx][ny] > cnt + 1:
                            visited_p[nx][ny] = True
                            p.append([nx, ny, cnt + 1])
                    else:  # 범위 밖 탈출
                        return cnt + 1
            else:
                return "IMPOSSIBLE"


        fire_lst = deque()
        start_px = 0
        start_py = 0

        for i in range(h):
            for j in range(w):
                if arr[i][j] == "*":   # 상근이 위치에서 시작
                    fire_lst.append([i, j])
                    visited_fire[i][j] = 0  # 시작위치는 0
                elif arr[i][j] == "@":
                    start_px = i
                    start_py = j
        burn(fire_lst)
        # print(visited_fire)
        print(person([start_px, start_py, 0]))


if __name__ == "__main__":
    # boj15665()
    # boj16987()
    boj5427()