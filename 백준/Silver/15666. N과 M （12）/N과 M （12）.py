def NM12():
    def f(i):  # i는 depth
        if i == M:
            print(' '.join(map(str, res)))
            return
        for j in range(len(arr)):
            if i == 0 or res[-1] <= arr[j]:
                res.append(arr[j])
                f(i+1)
                res.pop()

    N, M = map(int, input().split())
    # N개의 자연수 중에서 M개를 고른 수열
    # 같은 수를 여러번 골라도 되며, 고른 차순은 비내림차순 이어야 한다.
    arr = set(list(map(int, input().split())))
    arr = sorted(arr)
    res = []
    f(0)

NM12()