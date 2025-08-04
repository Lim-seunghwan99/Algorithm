import sys
sys.setrecursionlimit(10**5)

def find_friend(start):
    global result
    visited[start] = True
    path.append(start)
    nxt = students[start]
    if visited[nxt]:
        if nxt in path:
            result += len(path) - path.index(nxt)
        return
    else:
        find_friend(nxt)

T = int(input())
for _ in range(T):
    N = int(input())
    # 인덱스가 사람, students는 뽑은 사람
    # 순환이 안되면 팀 x
    students = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    result = 0
    for i in range(1, N + 1):
        if not visited[i]:
            path = []
            find_friend(i)
    print(N - result)
