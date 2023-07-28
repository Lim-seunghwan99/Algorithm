def group(): # 앞에쓰인 문자가 뒤에 쓰이면 count = 0
    n = int(input())
    count = 0
    for _ in range(n):
        r = []
        wordg = input()
        for i in wordg:
            if i not in r:
                r.append(i)
            elif r[-1] == i:
                continue
            else:
                count -= 1
                break
        count += 1
    return count

print(group())