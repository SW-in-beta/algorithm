import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
routers = sorted(int(input()) for _ in range(N))

def count(gap):
    prev = routers[0]
    cnt = 1
    for i in range(1, len(routers)):
        if routers[i] - prev < gap:
            continue
        cnt += 1
        prev = routers[i]
    return cnt

left = 0
right = (routers[-1] - routers[0]) // (C - 1)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = count(mid)
    if cnt < C:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1
print(answer)