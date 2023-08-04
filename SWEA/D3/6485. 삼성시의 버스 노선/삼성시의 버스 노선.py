def samsungbus():
    T = int(input()) # 테스트 케이스 개수
    for tc in range(1, T+1):
        N = int(input())# 하나의 정수
        res = []
        arr = [0] * 5001
        for i in range(N):
            Ai, Bi = list(map(int, input().split()))
            for j in range(Ai, Bi + 1):
                arr[j] += 1 
        P = int(input())
        for j in range(P):
            cj = int(input())
            res.append(arr[cj])
        print(f'#{tc}', end=' ')
        print(*res)
 
samsungbus()