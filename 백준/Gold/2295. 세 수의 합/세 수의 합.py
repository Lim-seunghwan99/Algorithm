def boj2295():
    N = int(input())
    U = sorted(int(input()) for _ in range(N))
    # 집합 U에서 적당히 세 수를 골랐을 때, 세 수의 합 d도 U안에 포함되는 경우가 있을 수 있다.
    # 이 경우들 중 가장 큰 d는?
    # 다른 풀이, 두 수를 합친 set 자료형을 만든 후, 큰 값부터 값 두개를 골라
    # 그 차가 set 자료형에 있다면, 세 수의 합도 U안에 있는 것과 같다.
    # 고정된 원소 찾는 이분탐색, 시간복잡도 log n

    # 세 가지 수를 골라서(이분탐색으로 그 수가 있는지 확인한다.)
    def binary_search(arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2 # 타겟인 숫자가 U의 부분 집합으로 구해질 수 있는가?
            if arr[mid] == target:
                return target
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # 중복된 수 고를 수 있음
    sum_list = []
    for i in range(N):
        for j in range(i, N):
            sum_list.append(U[i] + U[j])

    # 정렬 (이분 탐색을 위해)
    sum_list.sort()

    for i in range(N - 1, -1, -1):
        for j in range(N):
            target = U[i] - U[j]
            chk = binary_search(sum_list, target)
            if chk != -1:
                return chk + U[j]






if __name__ == "__main__":
    # boj15665()
    # boj16987()
    # boj5427()
    # boj13549()
    # boj18869()
    # boj2467()
    # boj14921()
    print(boj2295())