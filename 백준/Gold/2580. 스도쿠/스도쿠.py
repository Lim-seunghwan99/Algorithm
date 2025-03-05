# 1부터 9까지의 숫자가 한 번만 나타나야한다.
# 3 X 3 정사각형안에서도 1~9까지의 숫자가 한 번만 나타나야 한다.
# 빈칸은 0이 주어진다.
import pprint
# 문제 해결법 0위치에 들어갈 수 있는 경우의 수를 넣고, 재귀 돌리면서 제거하기
# 가로줄 체크, 세로줄 체크, 3X3 체크, 다른 8가지가 확정이기 때문에 우선적으로 들어가는 것 확정짓기기
# n이 가로에 있는지 확인
def row(a, n):
    for i in range(9):
        if n == sdoku[a][i]:
            return False
    return True

# n이 가로에 있는지 확인
def col(a, n):
    for i in range(9):
        if n == sdoku[i][a]:
            return False
    return True

def square(y, x, n):
    for i in range(3):
        for j in range(3):
            if n == sdoku[y//3 * 3 + i][x//3 * 3 + j]:
                return False
    return True


def chk(n):
    if n == len(chklst):
        for i in sdoku:
            print(*i)
        exit()

    for i in range(1, 10):
        y = chklst[n][0]
        x = chklst[n][1]
        if col(x, i) and row(y, i) and square(y, x, i):
            sdoku[y][x] = i
            chk(n+1)
            sdoku[y][x] = 0


sdoku = [list(map(int, input().split())) for _ in range(9)]
chklst = []
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            # 찾아야 할 값의 x, y를 chklst에 넣어준다.
            chklst.append([i,j])

chk(0)

for i in range(9):
    for j in range(9):
        # 만약 0이라면 빈칸에 추가
        if sdoku[i][j] == 0:
            chklst.append((i, j))
pprint.pprint(sdoku)