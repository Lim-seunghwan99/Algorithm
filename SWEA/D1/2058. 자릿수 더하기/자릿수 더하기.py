def sumdig():
    sum = 0
    a = input()
    for i in list(str(a)):
        sum += int(i)
    return(sum)

print(sumdig())