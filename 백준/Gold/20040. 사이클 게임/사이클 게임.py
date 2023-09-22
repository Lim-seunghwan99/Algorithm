def boj20040():
    # n, m
    # 0부터 n-1까지 고유한 번호가 부여,
    # 선 플레이어가 홀수 번째 차례를, 후 플레이어가 짝수 번째
    # 다 연결하면 끝
    # m번의 차례를 모두 처리한 후에도 종료되지 않았다면 0을 출력한다.
    # --> 사이클이 있으면 멈춰라
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nx = find(x)
        ny = find(y)

        if nx < ny:
            parent[ny] = nx
        else:
            parent[nx] = ny

    n, m = map(int, input().split())
    parent = [i for i in range(n)]

    ans = 0
    for i in range(1, m+1):
        s, t = map(int, input().split())
        if find(s) == find(t):
            ans = i
            break
        union(s, t)
    print(ans)


boj20040()