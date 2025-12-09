import sys
input = lambda: sys.stdin.readline().rstrip()
T, W = map(int, input().split())

dp = [0] * (W + 1)

for t in range(1, T+1):
    plum = int(input())
    flag = plum % 2
    dp[0] += flag
    for w in range(1, min(t+1, W+1)):
        w_flag = w % 2
        if flag != w_flag:
            dp[w] = max(dp[w], dp[w-1]) + 1
        else:
            dp[w] = max(dp[w], dp[w-1] - 1)

print(max(dp))