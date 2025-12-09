import sys
input = lambda: sys.stdin.readline().rstrip()
C, N = map(int, input().split())
INF = float('inf')
dp = [INF] * (C + 1)
dp[0] = 0

for _ in range(N):
    p, c = map(int, input().split())
    for i in range(1, C + 1):
        if i < c:
            dp[i] = min(dp[i], p)
        else:
            dp[i] = min(dp[i], dp[i-c] + p)

print(dp[-1])