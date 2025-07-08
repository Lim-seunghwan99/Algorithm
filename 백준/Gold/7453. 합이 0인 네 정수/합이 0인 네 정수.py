import sys
input = sys.stdin.readline
import heapq


def boj7453():
    n = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    # 1. 정렬을 해야 함
    # 2. 완탐 아님? -> 두 개씩 합 구한 후, 가지치기?
    ab_sums = []
    cd_sums = []

    for i in range(n):
        for j in range(n):
            ab_sums.append(A[i] + B[j])
            cd_sums.append(C[i] + D[j]) # D와 C의 합으로 수정

    ab_sums.sort() 
    cd_sums.sort(reverse=True)

    cnt, left, right = 0, 0, 0
    len_ab = len(ab_sums)
    len_cd = len(cd_sums)

    while left < len_ab and right < len_cd:
        chk = ab_sums[left] + cd_sums[right]

        if chk == 0:
            ab_chk = ab_sums[left]
            cd_chk = cd_sums[right]
            ab_cnt = 0
            cd_cnt = 0

            while left < len_ab and ab_sums[left] == ab_chk:
                ab_cnt += 1
                left += 1

            while right <len_cd and cd_sums[right] == cd_chk:
                cd_cnt += 1
                right += 1

            cnt += ab_cnt * cd_cnt


        elif chk < 0:
            left += 1

        else:
            right += 1

    print(cnt)




if __name__ == "__main__":
    boj7453()