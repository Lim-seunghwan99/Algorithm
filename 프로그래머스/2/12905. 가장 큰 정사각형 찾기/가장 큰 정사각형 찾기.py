def solution(board):
    dx = [0, -1, -1]
    dy = [-1, 0, -1]
    max_num = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            bp = 0
            if board[i][j] == 1:
                mx = 1e9
                for k in range(3):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < len(board) and 0 <= ny <len(board[i]):
                        if mx > board[nx][ny]:
                            mx = board[nx][ny]
                    else:
                        bp = 1
                        break
                if bp == 0:            
                    board[i][j] = mx + 1
            if max_num < board[i][j]:
                max_num = board[i][j]
                
                
    return max_num ** 2

    