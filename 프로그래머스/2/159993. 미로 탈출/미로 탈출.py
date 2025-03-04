def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    def bfs1(x, y):
        visited[x][y] = 1
        q = [(x, y)]
        while q:
            x, y = q.pop(0)
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[i]):
                    if visited[nx][ny] == 0 and arr[nx][ny] != 'X':
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        if arr[nx][ny] == 'L':
                            print(visited[nx][ny])
                            return (nx, ny, visited[nx][ny])
        else:
            return -1
    
    def bfs2(temp):
        x = temp[0]
        y = temp[1]
        q = [(x, y)]
        visited[x][y] = temp[2]
        temp[2]
        while q:
            x, y = q.pop(0)
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[i]):
                    if visited[nx][ny] == 0 and arr[nx][ny] != 'X':
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        if arr[nx][ny] == 'E':
                            return visited[x][y]
        
        else:
            return -1
                
            
        
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    arr = [list(maps[i]) for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if arr[i][j] == 'S':
                temp = bfs1(i, j)
                if temp != -1:
                    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
                    return bfs2(temp)
                else:
                    return temp
        
    