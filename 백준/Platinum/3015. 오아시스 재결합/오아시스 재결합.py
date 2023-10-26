from sys import stdin
HEIGHT, CNT = 0, 1
n = int(stdin.readline())
height = [int(stdin.readline()) for _ in range(n)]
stack = []
answer = 0

for h in height:
    while stack and stack[-1][HEIGHT] < h:
        answer += stack.pop()[CNT]

    if not stack:
        stack.append((h, 1))
    else:
        if stack[-1][HEIGHT] == h:
            cnt = stack.pop()[CNT]
            answer += cnt

            if stack:
                answer += 1

            stack.append((h, cnt + 1))
        else:
            stack.append((h, 1))
            answer += 1
print(answer)