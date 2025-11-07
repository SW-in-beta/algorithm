import sys
from heapq import heappush, heappop
input = lambda : int(sys.stdin.readline().rstrip())

h = []
res = []
for _ in range(input()):
    o = input()
    if o:
        heappush(h, (abs(o), o))
    else:
        res.append(str(heappop(h)[1] if h else 0))

print('\n'.join(res))