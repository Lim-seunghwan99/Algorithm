def solution(name):
# 두번 꺽는 경우는 고려하지 않음

    if set(name) == {'A'}:
        return 0

    a_pos = ord('A') # 'A' : 65, 'Z' : 90
    z_pos = ord('Z')

    answer = float('inf')

    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i] #왼쪽먼저 갔다가 + 오른쪽
        r_l = name[i: :-1] + name[i+1:][::-1] # 기준점에서 빠꾸 + 좌측
        for n in [l_r,r_l]:
            # 끝에 A들은 셀 필요 없으므로 자르기
            while n and n[-1] == 'A':
                n = n[:-1]
            cnt = [min(ord(c)-a_pos, (z_pos+1) - ord(c)) for c in n ]
            answer = min(answer, i + (len(cnt)-1) + sum(cnt))

    return answer
n = int(input())
for i in range(n):
    name = input()
    print(solution(name))