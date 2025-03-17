def boj15664():
    N, M = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    res = set()

    def back(idx, temp):
        if len(temp) == M:
            if not tuple(temp) in res:
                print(*temp)
                res.add(tuple(temp))
        for i in range(idx, N):
            temp.append(arr[i])
            back(i + 1, temp)
            temp.pop()


    back(0, [])

if __name__ == "__main__":
    # boj9935()
    # boj1182()
    # boj15655()
    # boj15656()
    boj15664()