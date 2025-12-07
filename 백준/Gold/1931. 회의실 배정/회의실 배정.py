import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
h = []
for _ in range(N):
    s, e = map(int, input().split())
    heappush(h, (e, s))

E = 0
cnt = 0
while h:
    e, s = heappop(h)
    if s < E:
        continue
    E = e
    cnt += 1
print(cnt)