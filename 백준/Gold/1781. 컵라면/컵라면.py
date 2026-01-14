import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tasks = []
for _ in range(N):
    deadline, cnt = map(int, input().split())
    tasks.append((deadline, cnt))
tasks.sort(reverse=True)
day = N
cnt = 0
i = 0
heap = []
while day >= 1:
    while i < N and tasks[i][0] >= day :
        heappush(heap, -tasks[i][1])
        i += 1
    if heap:
        cnt += -heappop(heap)
    day -= 1
    
print(cnt)