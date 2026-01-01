INF = float('inf')
step = list(map(int, input().split()))[:-1]
dp = [[INF] * 5 for _ in range(len(step))]
cost = (1, 3, 4, 3)

prev = step[0]
dp[0][0] = 2
for i in range(1, len(step)):
    cur = step[i]
    for j in range(5):
        if j == cur:
            continue
        if j != prev:
            dp[i][j] = dp[i-1][j] + cost[abs(prev - cur)]
        else:
            dp[i][j] = min(dp[i-1][0] + 2,*[dp[i-1][k] + cost[abs(cur - k)] for k in range(1, 5)])
    prev = cur
    
print(min(dp[-1]))