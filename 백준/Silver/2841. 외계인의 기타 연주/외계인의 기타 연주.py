from bisect import bisect_right
import sys
input = lambda: sys.stdin.readline().rstrip()

N, P = map(int, input().split())
lines = [None] + [[0] for _ in range(6)]
cnt = 0

for _ in range(N):
    line,  fret = map(int, input().split())
    pos = bisect_right(lines[line], fret)
    cnt += len(lines[line]) - pos
    lines[line] = lines[line][:pos]
    if lines[line][-1] < fret:
        cnt += 1
        lines[line].append(fret)
print(cnt)