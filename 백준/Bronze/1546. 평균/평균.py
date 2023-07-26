def cheat():
    n = int(input())
    score = list(map(int, input().split()))
    sv = 0
    for i in score:
        sv += (i/max(score)*100)
    avg = sv/n
    return avg
print(cheat())