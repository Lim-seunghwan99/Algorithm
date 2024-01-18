def solution(n, s):
    answer = []
    temp = s / n
    if(temp == int(temp)):  # 그냥 같은 값이 여러개
        for i in range(n):
            answer.append(temp)
    else:
        if temp < 1:
            return [-1]
        while n >= 1:
            answer.append(s // n)
            s -= s // n
            n -= 1
            
    return answer