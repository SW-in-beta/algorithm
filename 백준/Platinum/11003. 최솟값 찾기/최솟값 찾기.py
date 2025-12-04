from collections import deque

INF = float('inf')
N, L = map(int, input().split())
q = deque()

for i, e in enumerate(map(int, input().split())):
    while q and q[0][0] <= i - L:
        q.popleft()
    while q and q[-1][1] >= e:
        q.pop()
    q.append((i, e))
    print(q[0][1], end=" ")