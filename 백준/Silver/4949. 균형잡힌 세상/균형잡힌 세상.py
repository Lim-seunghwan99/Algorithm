while True:
    arr = input()
    opr = []
    bre = 0
    if arr == '.':
        bre = 1
        break
    for s in arr:
        if s in ['(', '[']:
            opr.append(s)
        if s in [')', ']']:
            if len(opr) > 0:
                t = opr.pop()
                if s == ')' and t == '[':
                    bre = 1
                    break
                elif s == ']' and t == '(':
                    bre = 1
                    break
            else:
                bre = 1
                break
            if bre == 1:
                break
    if bre == 1 or len(opr) > 0:
        print('no')
    else:
        print('yes')