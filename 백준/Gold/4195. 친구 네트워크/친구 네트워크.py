def BOJ4195():

    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x != y:
            parents[x] = y
            cnt[y] += cnt[x]

    T = int(input())
    for _ in range(T):
        friends = dict()
        F = int(input())
        idx = -1
        a = b = 0
        parents = [i for i in range(200000)]
        cnt = [1 for _ in range(200000)]
        for i in range(F):
            s1, s2 = input().split()
            if s1 in friends:
                a = friends.get(s1)
            else:
                idx += 1
                friends[s1] = idx
                a = idx
            if s2 in friends:
                b = friends.get(s2)
            else:
                idx += 1
                friends[s2] = idx
                b = idx
            union(a, b)
            print(cnt[find(a)])

BOJ4195()