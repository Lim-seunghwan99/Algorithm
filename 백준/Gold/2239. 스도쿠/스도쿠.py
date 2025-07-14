import sys
input = sys.stdin.readline


def chkrow(r, num):
    return num not in arr[r]


def chkcol(c, num):
    for i in range(9):
        if arr[i][c] == num:
            return False
    return True


def chkbox(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[nr + i][nc + j] == num:
                return False
    return True


def dfs():
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                for k in range(1, 10):
                    if chkrow(i, k) and chkcol(j, k) and chkbox(i, j, k):
                        arr[i][j] = k
                        if dfs():
                            return True
                        arr[i][j] = 0
                return False
    return True


def boj2239():
    global arr
    arr = [list(map(int, input().strip())) for _ in range(9)]

    # dfs()가 True를 반환하면 (즉, 성공하면) 결과를 출력합니다.
    if dfs():
        for row in arr:
            # 출력 형식 수정: [1, 2, 3] -> "123"
            print("".join(map(str, row)))


if __name__ == "__main__":
    boj2239()