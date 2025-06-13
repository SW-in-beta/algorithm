from collections import deque

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

parents = [0] * (N + 1)
queue = deque([1])
while queue:
    node = queue.popleft()
    for next_node in edges[node]:
        if parents[next_node]:
            continue
        parents[next_node] = node
        queue.append(next_node)
print(*parents[2:], sep='\n')
