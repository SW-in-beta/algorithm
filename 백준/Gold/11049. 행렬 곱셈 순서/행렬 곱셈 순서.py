import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
INF = float('inf')
dp = [[INF] * N for _ in range(N)]
matrix = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    dp[i][i] = 0
    
for s in range(1, N):
    for i in range(N-s):
        j = i + s
        n, m = matrix[i][0], matrix[j][1]
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp [k+1][j] + n * m * matrix[k][1])
            
print(dp[0][-1])