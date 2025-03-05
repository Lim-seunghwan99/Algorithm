import sys
input = sys.stdin.readline

# N: 장애물 개수, H: 동굴 높이
N, H = map(int, input().split())

# 석순(아래에서 올라오는 장애물)과 종유석(위에서 내려오는 장애물) 개수 저장
down = [0] * (H + 1)
up = [0] * (H + 1)

# 입력 받기
for i in range(N):
    height = int(input())
    if i % 2 == 0:
        down[height] += 1  # 석순
    else:
        up[H - height + 1] += 1  # 종유석

for i in range(1, H + 1):
    up[i] = up[i - 1] + up[i]
    # 역순으로 내려와야 함
    # i가 7일때, 6이랑 비교하고 6 = 7 + 6
    # i가 6일때, 5이랑 비교하고 5 = 6 + 5
    down[H - i] = down[H - i + 1] + down[H - i]
    # down[6] = down[7] + down[6]
    # down[5] = down[6] + down[5]
    # down[0] = down[1] + down[0]

obstacle = 1e6
cnt = 0


for i in range(1, H + 1):
    if down[i] + up[i] < obstacle:
        obstacle = down[i] + up[i]
        cnt = 1
    elif down[i] + up[i] == obstacle:
        cnt += 1

print(obstacle, cnt)
