n = int(input())
s = list(input().split())
mx = []
mn = []
mx_lst = [i for i in range(10)]
mn_lst = [i for i in range(10)]
cnt = 0
mx_stack = []
for i in range(len(s)):
    if s[i] == '<':
        mx_stack.append('<')
    elif s[i] == '>':
        mx_stack.append('>')
        while mx_stack:
            mx.append(mx_lst.pop(len(mx_lst) - len(mx_stack)))
            mx_stack.pop()
if mx_stack:
    while mx_stack:
        mx.append(mx_lst.pop(len(mx_lst) - (len(mx_stack)+1)))
        mx_stack.pop()
mx.append((mx_lst.pop()))

mn_stack = []
for i in range(len(s)):
    if s[i] == '>':
        mn_stack.append('>')
    elif s[i] == '<':
        mn_stack.append('<')
        while mn_stack:
            mn.append(mn_lst.pop(len(mn_stack)-1))
            mn_stack.pop(0)
if mn_stack:
    while mn_stack:
        mn.append(mn_lst.pop(len(mn_stack)))
        mn_stack.pop(0)
mn.append((mn_lst.pop(0)))
res1 = ''
for i in range(len(mx)):
   res1 += str(mx[i])
print(res1)
res2 = ''
for j in range(len(mn)):
    res2 += str(mn[j])
print(res2)