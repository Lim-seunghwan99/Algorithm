def boj2467():
    N = int(input())
    arr = list(map(int, input().split()))  # 정렬된 상태로 주어진다.
    # 0에 가장 가까운 용액을 만들어 내는 두 용액의 특성값을 출력한다. (오름차순)
    # 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상인 경우, 아무거나 출력
    left = 0
    right = len(arr) - 1
    res = 10**12
    ans1 = 10**12
    ans2 = 10**12
    while left < right:
        # 두 개의 합을 구한 후, 만약 +라면 right - 1, 반대면 left + 1
        chk = arr[left] + arr[right]
        if chk == 0:
            ans1 = arr[left]
            ans2 = arr[right]
            break
        elif chk > 0:
            if abs(res) > abs(chk):
                ans1 = arr[left]
                ans2 = arr[right]
                res = abs(chk)
            right -= 1
        elif chk < 0:
            if abs(res) > abs(chk):
                ans1 = arr[left]
                ans2 = arr[right]
                res = abs(chk)
            left += 1
    print(ans1, ans2)


if __name__ == "__main__":
    # boj15665()
    # boj16987()
    # boj5427()
    # boj13549()
    # boj18869()
    boj2467()