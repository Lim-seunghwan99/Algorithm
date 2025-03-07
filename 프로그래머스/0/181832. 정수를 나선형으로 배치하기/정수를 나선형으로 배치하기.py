dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def solution(n):
    answer = [[0] * n for _ in range(n)]
    cnt = 2
    k = 0
    x, y = 0, 0
    answer[y][x] = 1
    while cnt <= n**2:
        k %= 4
        if 0 <= y + dy[k] < n and 0 <= x + dx[k] < n:
            if answer[x + dx[k]][y + dy[k]] > 0:
                k += 1
                continue
            x = x + dx[k]
            y = y + dy[k]
            answer[x][y] = cnt
            cnt += 1
        else:
            # 만약 벗어났다면, dx, dy를 한칸 밖으로
            k += 1
    return answer