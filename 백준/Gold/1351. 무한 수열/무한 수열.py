N, P, Q = map(int, input().split())
dp = {0:1}

def seq(n):
    if n not in dp:
        dp[n] = seq(n // P) + seq(n // Q)
    return dp[n]

print(seq(N))