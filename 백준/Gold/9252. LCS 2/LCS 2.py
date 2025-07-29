str1 = input()
str2 = input()
dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

# 메모이제이션으로 최대 수열의 값 찾기
for i in range(1, len(str1) + 1):
    for j in range(1,len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ""
chk1, chk2 = len(str1), len(str2)
# dp 역추적으로 문자 찾기
while chk1 > 0 and chk2 > 0:
    if str1[chk1 - 1] == str2[chk2 - 1]:
        ans += str1[chk1 - 1]
        chk1 -= 1
        chk2 -= 1
    else:
        if dp[chk1 - 1][chk2] > dp[chk1][chk2 - 1]:
            chk1 -= 1
        else:
            chk2 -= 1

print(dp[len(str1)][len(str2)])
print(ans[::-1])