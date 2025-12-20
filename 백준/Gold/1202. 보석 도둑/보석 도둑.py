import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, K = map(int, input().split())
jewelries = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewelries.sort()
bags.sort()

result = 0
idx = 0
max_heap = []

for bag in bags:
    while idx < N and jewelries[idx][0] <= bag:
        heappush(max_heap, -jewelries[idx][1])
        idx += 1

    if max_heap:
        result += -heappop(max_heap)

print(result)