def boj9935():
    words = input()
    bomb = input()
    stk = list(words)
    # 폭발이 터지면, 폭발 문자열 개수 만큼만 pop한 후 다시 넣으면서 확인하기?
    ans = []
    while stk:
        tmp = stk.pop()
        # 체크 알고리즘
        if tmp == bomb[0]:
            for i in range(1, len(bomb)): # 첫 글자는 이미 같다.
                if ans:
                    if bomb[i] != ans[len(ans) - i]:
                        break
                else:
                    break
            else:
                # 폭탄!!
                for j in range(1, len(bomb)):
                    ans.pop()
                continue
        ans.append(tmp)
    if ans:
        print(''.join(reversed(ans)))
    else:
        print("FRULA")



if __name__ == "__main__":
    boj9935()