from heapq import heappush, heappop
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
queue = []
for _ in range(n):
    h, o = map(int, input().split())
    queue.append((max(h, o), min(h, o)))

queue = deque(sorted(queue))
d = int(input())

heap = []
cnt = 0

while queue:
    end = queue[0][0]
    start = end - d
    
    while heap and heap[0][0] < start:
        heappop(heap)
        
    while queue and queue[0][0] <= end:
        o, h = queue.popleft()
        if h >= start:
            heappush(heap, (h, o))
    
    cnt = max(cnt, len(heap))
    
print(cnt)       