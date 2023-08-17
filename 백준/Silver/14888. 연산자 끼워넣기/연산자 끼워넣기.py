N = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
# 숫자는 고정하고 오퍼레이터를 순열 돌린다.
stack = []
if oper[0] > 0:
    for i in range(oper[0]):
        stack.append('+')
if oper[1] > 0:
    for i in range(oper[1]):
        stack.append('-')
if oper[2] > 0:
    for i in range(oper[2]):
        stack.append('*')
if oper[3] > 0:
    for i in range(oper[3]):
        stack.append('/')
#print(stack)
# +, -, *, /
# 완전 탐색
# 숫자 하나 oper하나 나와야 한다.
mi = 1000000000
mx = -1000000000
res = []


def f(i, N, sv):
    global mx
    global mi
    if i == len(stack):
        for k in range(len(stack)):
            if stack[k] == '+':
                sv += arr[k+1]
            elif stack[k] == '-':
                sv -= arr[k+1]
            elif stack[k] == '*':
                sv *= arr[k+1]
            elif stack[k] == '/':
                if sv < 0:
                    sv = -sv
                    sv //= arr[k+1]
                    sv = -sv
                else:
                    sv //= arr[k+1]
        mx = max(mx, sv)
        mi = min(mi, sv)
    else:
        for j in range(i, len(stack)):
            stack[i], stack[j] = stack[j], stack[i]
            f(i+1, N, sv)
            stack[i], stack[j] = stack[j], stack[i]
            sv = arr[0]


f(0, N, arr[0])
print(mx, mi)