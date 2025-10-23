import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())
edges = [set() for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].add(v)
    edges[v].add(u)

def search(v, dfs=True):
    sorted_edges = [sorted(edge, reverse=dfs) for edge in edges]
    queue = deque([v])
    visited = [False] * (N + 1)
    res = []
    while queue:
        e = queue.pop() if dfs else queue.popleft()
        if visited[e]:
            continue
        visited[e] = True
        res.append(str(e))

        for node in sorted_edges[e]:
            if visited[node]:
                continue
            queue.append(node)
            
    return res
        
print(' '.join(search(V)))
print(' '.join(search(V, False)))