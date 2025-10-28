import sys
import math
from heapq import heappush, heappop
input = lambda : sys.stdin.readline().rstrip()

V, E = map(int, input().split())
K = int(input())

es = [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  es[u].append((v, w))

vs = [math.inf] * (V+1)
heap = [(0, K)]

while len(heap) > 0:
  d, u = heappop(heap)
  if vs[u] < d: continue
  vs[u] = d
  for v, w in es[u]:
    if d + w >= vs[v]: continue
    vs[v] = d + w
    heappush(heap, (d+w, v))

print('\n'.join(map(lambda x: str(x).upper(), vs[1:])))