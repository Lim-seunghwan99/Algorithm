from collections import deque
def bfs(si,sj):
    q = deque()
    vv = [[0]*5 for _ in range(5)]

    q.append((si,sj))
    vv[si][sj]=1
    cnt = 1

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and vv[ni][nj]==0 and v[ni][nj]==1:
                q.append((ni,nj))
                vv[ni][nj]=1
                cnt+=1
    return cnt==7

def check():
    for i in range(5):
        for j in range(5):
            if v[i][j]==1:
                return bfs(i,j)

def dfs(n, cnt, scnt):
    global ans
    if cnt>7:                  
        return

    if n == 25:
        if cnt==7 and scnt>=4:  
            if check():         
                ans+=1
        return

    v[n//5][n%5]=1              
    dfs(n+1, cnt+1, scnt+int(arr[n//5][n%5]=='S'))
    v[n//5][n%5]=0              
    dfs(n+1, cnt, scnt)         

arr = [input() for _ in range(5)]
ans = 0
v = [[0]*5 for _ in range(5)]
dfs(0, 0, 0)
print(ans)