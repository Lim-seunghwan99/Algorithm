# 괄호열은 (), []만 사용한다.
# () 의 괄호열은 2이다.
# [] 인 괄효열은 3이다.
# (x)의 괄호값은 2*x, [x]는 3*x
# xy의 괄호값은 (xy) = (x)+(y)
arr = list(input())
stack = []
ans = 0
temp = 1
res = []
for i in range(len(arr)):
    if arr[i] == '(':
        temp *= 2
        stack.append(arr[i])
    elif arr[i] == '[':  # 여는 괄호일 경우
        temp *= 3
        stack.append(arr[i])
    else:  # 닫는 괄호일 경우
        if stack:
            if arr[i] == ')':
                if stack[-1] == '(':  # 괄호 매칭
                    if arr[i-1] == '(':
                        ans += temp
                    stack.pop()
                    temp //= 2
                else:  # 괄호 매칭 안될 때
                    ans = 0
                    break
            elif arr[i] == ']':
                if stack[-1] == '[':
                    if arr[i - 1] == '[':
                        ans += temp
                    stack.pop()
                    temp //= 3
                else:  # 괄호 매칭 안될 때
                    ans = 0
                    break
        else:  # 여는 괄호가 없는 경우 0
            ans = 0
            break
if stack:  # 스택에 여는 연산자가 남는 경우
    ans = 0
print(ans)