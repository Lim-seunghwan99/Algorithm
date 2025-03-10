S = input()
q = int(input())
# 특정 문자열에서, 특정 알파벳과 문자열의 구간이 주어지면,
# 문자열 S의 l부터 r사이에 a가 몇 번 나타나는지 구하는 프로그램을 작성하라.

dp = [{} for _ in range(len(S))]
# r - l 의 누적합을 구하면 된다.
# 리스트에 딕셔너리를 n개 만든다.?
dp[0] = {S[0]:1}
for i in range(1, len(S)):
    dp[i].update(dp[i - 1])
    if S[i] in dp[i - 1]:
        dp[i][S[i]] += 1
    else:
        dp[i][S[i]] = 1
for i in range(q):
    a, l, r = input().split()
    if int(l) == 0:
        print(dp[int(r)].get(a, 0))
    else:
        print(dp[int(r)].get(a, 0) - dp[int(l) - 1].get(a, 0))