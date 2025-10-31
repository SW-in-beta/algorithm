import sys
from heapq import heappush, heappop
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
h = []
for i in range(N):
    for e in map(int, input().split()):
        heappush(h, e)
        if i >= 1:
            heappop(h)
        
print(sorted(h)[0])