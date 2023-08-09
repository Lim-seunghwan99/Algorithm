def meetingroom3():
    N = int(input())
    # 시간대 다 집어넣고, 최대 개수 출력
    res = []
    for _ in range(N):
        [si, ei] = list(map(int, input().split()))
        res.append([si, ei])
    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[1])
		# 시작 시간으로 정렬한 다음 끝나는 시간으로 정렬한다
		# why? (9,10), (10,10)이 있는 경우 끝나는 시간으로 정렬하면 10,10다음 9,10이 올 수 있어.
		# 근데 그냥 sort해도 시작시간 끝나는 시간으로 정렬되지 않을까? -> 아니였다.
		# 위의 경우는 이중포문으로 시간이 오래걸림
		# 시간순으로 정렬시 일일히 비교할 필요가 없어 시간복잡도가 크게 줄어듬
    cnt = 1
    time = res[0][1]
    for j in range(1, N): #i
        if time <= res[j][0]:
            time = res[j][1]
            cnt += 1
    print(cnt)


meetingroom3()