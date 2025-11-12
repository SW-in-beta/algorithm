import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

for _ in range(int(input())):
    N = int(input())
    dp = [[INF] * N for _ in range(N)]
    k = [[0] * N for _ in range(N)]
    seq = tuple(map(int, input().split()))
    a_sum = [0] * (N + 1)
    a = 0
    for i, s in enumerate(seq):
        a += s
        a_sum[i+1] = a
    for step in range(N):
        for start in range(N-step):
            if step == 0:
                dp[start][start] = 0
                k[start][start] = start
                continue
            end = start + step
            ls = a_sum[end + 1] - a_sum[start]
            if step == 1:
                dp[start][end] = ls
                k[start][end] = start
                continue
            
            dp[start][end], k[start][end] = min((dp[start][mid] + dp[mid + 1][end], mid) for mid in range(k[start][end-1], k[start+1][end] + 1))
            dp[start][end] += ls
                    
    print(dp[0][N-1])