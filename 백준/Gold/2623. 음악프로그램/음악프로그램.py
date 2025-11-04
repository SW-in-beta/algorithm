import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
edges = [0] * (N+1)
graph = [[] for _ in range(N+1)]
seq = []
for _ in range(M):
    sub = tuple(map(int, input().split()))
    for i in range(1, len(sub) - 1):
        u, v = sub[i], sub[i+1]
        graph[u].append(v)
        edges[v] += 1

q = [i for i in range(1, N+1) if edges[i] == 0]
while q:
    u = q.pop()
    seq.append(u)
    for v in graph[u]:
        edges[v] -= 1
        if edges[v] == 0:
            q.append(v)
            
if len(seq) < N:
    print(0)
else:
    print('\n'.join(map(str, seq)))