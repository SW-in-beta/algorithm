N = int(input())
dp = [0] * (N + 1)
cnt = 0
for e in map(int, input().split()):
    dp[e] = dp[e-1] + 1
    cnt = max(cnt, dp[e])
    
print(N - cnt)