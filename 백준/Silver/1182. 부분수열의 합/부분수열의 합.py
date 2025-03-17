def boj1182():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    # 합이 S가 되는 부분수열의 개수를 출력한다.
    ans = 0
    cnt = 0
    def subset_sum(idx, sub_sum):
        nonlocal cnt

        if idx >= N:
            return

        sub_sum += arr[idx]

        if sub_sum == S:
            cnt += 1

        # 현재 arr[idx]를 선택한 경우
        subset_sum(idx+1, sub_sum)
        # 현재 arr[idx]를 선택하지 않은 경우
        subset_sum(idx+1, sub_sum - arr[idx])

    subset_sum(0, 0)
    print(cnt)



if __name__ == "__main__":
    # boj9935()
    boj1182()