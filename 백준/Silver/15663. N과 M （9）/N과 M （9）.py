n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    t = 0
    for i in range(n):
        if not visited[i] and t != arr[i]:
            visited[i] = True
            temp.append(arr[i])
            t = arr[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()