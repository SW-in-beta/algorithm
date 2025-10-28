import sys
from heapq import heappush, heappop
input = lambda : sys.stdin.readline().rstrip()

V, E = map(int, input().split())
K = int(input())

dist = ['INF'] * (V+1)
h = [(0, K)]
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    
while h:
    w, u = heappop(h)
    if dist[u] != 'INF':
        continue
    dist[u] = w

    for nw, v in graph[u]:
        if dist[v] == 'INF':
            heappush(h, (w + nw, v))
            
print('\n'.join(map(str, dist[1:])))