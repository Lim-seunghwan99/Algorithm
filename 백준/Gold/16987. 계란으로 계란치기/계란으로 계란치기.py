def boj16987():
    from copy import deepcopy
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 내구도 S, 무게 W
    # 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제였다
    answer = 0

    def back(idx):
        nonlocal answer
        if idx == N:
            temp = 0
            for i in range(N):
                if arr[i][0] <= 0:
                    temp += 1
            answer = max(temp, answer)
            return

        if arr[idx][0] <= 0:
            back(idx + 1)
            return

        check = True
        # 깨야할 계란이 있는지 확인하는 코드
        for i in range(N): 
            if i == idx:
                continue
            if arr[i][0] > 0: 
                check = False
                break

        if check:
            answer = max(answer, N - 1)
            return

        for i in range(N):
            if i==idx or arr[i][0] <= 0:
                continue
            # 계란 부딪히기
            arr[idx][0] -= arr[i][1]
            arr[i][0] -= arr[idx][1]
            back(idx + 1)
            arr[idx][0] += arr[i][1]
            arr[i][0] += arr[idx][1]

    back(0)
    print(answer)





if __name__ == "__main__":
    # boj15665()
    boj16987()