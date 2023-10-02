def boj8983():
    m, n, l = map(int, input().split())  # 사대의 수, 동물의 수, 사정거리
    x_arr = list(map(int, input().split()))  # 사대의 위치
    # 각 동물의 사는 위치
    anml = [list(map(int, input().split())) for _ in range(n)]
    # 사대의 위치와 동물의 위치 간의 거리는 abs(xi-aj) + bj
    # 이분 탐색..?
    x_arr.sort()
    anml.sort()
    cnt = 0
    for i in range(len(anml)):
        for j in range(len(x_arr)):
            if abs(anml[i][0] - x_arr[j]) + anml[i][1] <= l:
                # print(f'{anml[i]} {x_arr[j]} {abs(anml[i][0] - x_arr[j]) + anml[i][1]}')
                cnt += 1
                break
    print(cnt)


boj8983()