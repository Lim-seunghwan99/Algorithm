def boj2467():
    N = int(input())
    arr = list(map(int, input().split()))
    left = 0
    right = N - 1
    res = float('inf')  # 초기값을 충분히 크게 설정
    ans1 = ans2 = 0

    while left < right:
        chk = arr[left] + arr[right]
        if abs(chk) < res:
            res = abs(chk)
            ans1 = arr[left]
            ans2 = arr[right]
            if chk == 0:  # 완전한 정답이면 바로 끝내기
                break
        if chk < 0:
            left += 1
        else:
            right -= 1

    print(ans1, ans2)






if __name__ == "__main__":
    # boj15665()
    # boj16987()
    # boj5427()
    # boj13549()
    # boj18869()
    boj2467()