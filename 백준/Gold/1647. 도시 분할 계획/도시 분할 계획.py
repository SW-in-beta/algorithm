import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parents = [i for i in range(N+1)]

def find(u):
    if parents[u] != u:
        parents[u] = find(parents[u])
    return parents[u]

def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return False
    parents[pu] = pv
    return True
    
h = []
for _ in range(M):
    u, v, c = map(int, input().split())
    heappush(h, (c, u, v))

total = 0
cnt = 0
while h and cnt < N - 2:
    c, u, v = heappop(h)
    if not union(u, v):
        continue
    total += c
    cnt += 1
    
print(total)