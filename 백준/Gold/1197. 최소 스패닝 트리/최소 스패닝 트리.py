import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())
P = [i for i in range(V+1)]
def find(v):
    if P[v] != v:
        P[v] = find(P[v])
    return P[v]

def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return False
    P[pu] = P[pv]
    return True

h = []
for _ in range(E):
    a, b, c = map(int, input().split())
    heappush(h, (c, a, b))

cost = 0
cnt = 0
while h and cnt < V - 1:
    c, a, b = heappop(h)
    if union(a, b):
        cnt += 1
        cost += c    

print(cost)