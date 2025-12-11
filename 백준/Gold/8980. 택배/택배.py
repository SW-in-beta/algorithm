import sys
from collections import deque
input = sys.stdin.readline

N, C = map(int, input().split())
truck = [0] * (N+1)
M = int(input())
l = []
for _ in range(M):
    s, e, w = map(int, input().split())
    l.append((e, s, w))

l.sort()
l = deque(l)
total = 0

while l:
    e, s, w = l.popleft()
    max_box = w
    for i in range(s, e):
        max_box = min(max_box, C - truck[i])
        if max_box == 0:
            break
    
    total += max_box
    if max_box:
        for i in range(s, e):
            truck[i] += max_box

print(total)