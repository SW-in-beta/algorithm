import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())
edges = [set() for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].add(v)
    edges[v].add(u)

sorted_edges = [sorted(edge, reverse=True) for edge in edges]
queue = deque([V])
visited = [False] * (N + 1)
dfs = []
while queue:
    e = queue.pop()
    if visited[e]:
        continue
    visited[e] = True
    dfs.append(str(e))

    for node in sorted_edges[e]:
        if visited[node]:
            continue
        queue.append(node)

sorted_edges = [sorted(edge) for edge in edges]        
queue = deque([V])
visited = [False] * (N + 1)    
bfs = []
while queue:
    e = queue.popleft()
    if visited[e]:
        continue
    visited[e] = True
    bfs.append(str(e))

    for node in sorted_edges[e]:
        if visited[node]:
            continue
        queue.append(node)
        
print(' '.join(dfs))
print(' '.join(bfs))