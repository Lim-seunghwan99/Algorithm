def cheat():
    n = int(input())
    score = list(map(int, input().split()))
    sv = 0
    return sum([i/max(score)*100 for i in score])/n
print(cheat())