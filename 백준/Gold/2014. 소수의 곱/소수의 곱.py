from heapq import heappush, heappop
K, N = map(int, input().split())
primes = tuple(map(int, input().split()))

h = list(primes)

while True:
    e = heappop(h)
    N -= 1
    if N == 0:
        break
    for p in primes:
        heappush(h, e * p)
        if e % p == 0:
            break
    
print(e)