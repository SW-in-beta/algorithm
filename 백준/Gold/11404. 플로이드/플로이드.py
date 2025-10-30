import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
INF = float('inf')
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    i, j, w = map(int, input().split())
    dist[i][j] = min(dist[i][j], w)
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

result = '\n'.join(' '.join(str(c) if c != INF else '0' for c in r[1:]) for r in dist[1:])
print(result)