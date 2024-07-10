s = input()
ans = 0
stack = []
for i in s:
    if i == '(':
        stack.append([int(temp), ans -1])
        ans = 0
    elif i == ')':
        k, prev = stack.pop()
        ans = k * ans + prev
    else:
        ans += 1
        temp = i
print(ans)