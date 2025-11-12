import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

for _ in range(int(input())):
    N = int(input())
    dp = [[INF] * N for _ in range(N)]
    seq = tuple(map(int, input().split()))
    a_sum = [0] * N
    a = 0
    for i, s in enumerate(seq):
        a += s
        a_sum[i] = a
    for step in range(N):
        for start in range(N-step):
            if step == 0:
                dp[start][start] = 0
                continue
            end = start + step
            ls = a_sum[end] - (a_sum[start - 1] if start else 0)
            dp[start][end] = min(dp[start][mid] + dp[mid + 1][end] for mid in range(start, end)) + ls
                    
    print(dp[0][N-1])