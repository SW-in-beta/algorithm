from collections import deque
N, L = map(int, input().split())
leaks = deque(sorted((map(int, input().split()))))

cnt = 1
left = leaks.popleft()
while leaks:
    e = leaks.popleft()
    if e - left < L:
        continue
    cnt += 1
    left = e

print(cnt)