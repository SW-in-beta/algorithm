import sys
from heapq import heappush, heappop
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
lh = [10001]
rh = [10001]
res = [None] * N
for i in range(N):
    e = int(input())
    flag = e > -lh[0]
    heappush(rh if flag else lh, e if flag else -e)
    if len(rh) > len(lh):
        heappush(lh, -heappop(rh))
    elif len(lh) > len(rh) + 1:
        heappush(rh, -heappop(lh))
    res[i] = str(-lh[0])
    
print('\n'.join(res))