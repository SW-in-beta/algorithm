s1 = '0' + input()
s2 = '0' + input()
dp = [[''] * len(s2) for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) >= len(dp[i][j-1]) else dp[i][j-1]
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i] if len(dp[i-1][j-1]) >= len(dp[i][j]) else dp[i][j]

print(len(dp[-1][-1]))
print(dp[-1][-1])