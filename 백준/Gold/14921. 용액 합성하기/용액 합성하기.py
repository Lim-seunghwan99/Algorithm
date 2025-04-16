def boj14921():
    N = int(input())
    arr = list(map(int, input().split()))  # 오름차순으로 주어진다.
    left = 0
    right = len(arr) - 1
    # 0에 가장 가까운 용액 만들기
    res = 10 ** 13
    while left < right:
        chk = arr[left] + arr[right]
        if chk == 0:
            res = 0
            break
        elif chk > 0:
            if abs(res) > abs(chk):
                res = chk
            right -= 1
        elif chk < 0:
            if abs(res) > abs(chk):
                res = chk
            left += 1
    print(res)


if __name__ == "__main__":
    # boj15665()
    # boj16987()
    # boj5427()
    # boj13549()
    # boj18869()
    # boj2467()
    boj14921()