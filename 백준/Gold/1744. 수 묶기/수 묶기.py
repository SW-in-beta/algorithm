from heapq import heappush, heappop
ph = []
nh = []

N = int(input())
for _ in range(N):
    num = int(input())
    if num > 0:
        heappush(ph, -num)
    else:
        heappush(nh, num)

res = 0

while len(ph) > 1:
    a = heappop(ph)
    b = heappop(ph)
    if a == -1 or b == -1:
        res += -a + -b
        break
    res += a * b

res += sum(map(abs, ph))

while len(nh) > 1:
    a = heappop(nh)
    b = heappop(nh)
    res += a * b

res += sum(nh)

print(res)