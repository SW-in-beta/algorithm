from heapq import heappush, heappop
    
MAX = 2 ** 31
K, N = map(int, input().split())
primes = tuple(map(int, input().split()))

heap = [1]

for _ in range(N):
    item = heappop(heap)
    for p in primes:
        val = item*p
        if val >= MAX:
            continue
        heappush(heap, val)
        if item % p == 0:
            break

print(heap[0])