N,X = map(int,input().split())
bur = [1] * 51            
pat = [1] * 51

for i in range(1, N+1):
    bur[i] = 2 * bur[i-1] + 3
    pat[i] = 2 * pat[i-1] + 1 

def eat(n, x):        
    if n == 0:
        return x
    if x == 1:
        return 0
    elif x <= 1 + bur[n-1]:   
        return eat(n-1, x-1)  
    elif x == 1 + bur[n-1] + 1:
        return pat[n-1] + 1
    elif x <= bur[n-1] + bur[n-1] + 1 + 1:  
        return pat[n-1] + 1 + eat(n-1, (x-(bur[n-1]+2)))
    else:                     
        return pat[n]

print(eat(N, X))