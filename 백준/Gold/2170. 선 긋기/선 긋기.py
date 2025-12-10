import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()
y = lines[0][0]
length = 0

for l in lines:
    length += max(l[1] - max(y, l[0]), 0)
    y = max(l[1], y)

print(length)