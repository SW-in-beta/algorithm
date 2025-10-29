import sys
import math
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
dist = [math.inf] * (N+1)
dist[1] = 0

for _ in range(N-1):
    for u, v, w in edges:
        if dist[u] != math.inf and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            
for u, v, w in edges:
    if dist[u] != math.inf and dist[v] > dist[u] + w:
        print(-1)
        exit()

for d in dist[2:]:
    print(d if d != math.inf else -1)