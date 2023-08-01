def swea9386():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        arr = list(map(int, input()))
        #arr = input().split('0') #0으로 나눠서 스트링 길이가 젤 긴거
        #스트링으로 해서 1이 연속해서 나오면 cnt++ max_cnt = cnt 계속 바꾸는 방법
        max_cnt = 0
        cnt = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                cnt = 0
            elif arr[i] == 1:
                cnt += 1
                if max_cnt <= cnt:
                    max_cnt = cnt
        print(f'#{tc} {max_cnt}')
swea9386()