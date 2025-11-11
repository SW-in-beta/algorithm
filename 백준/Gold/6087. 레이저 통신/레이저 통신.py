import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

C, R = map(int, input().split())
board = tuple(tuple(input()) for _ in range(R))
Cs = []

for r in range(R):
    for c in range(C):
        if board[r][c] == 'C':
            Cs.append((r, c))
sr, sc = Cs[0]
er, ec = Cs[1]
INF = float('inf')
md = ((1, 0), (0, 1), (-1, 0), (0, -1))
def next_i(r, c, d):
    return ((0 if d == nd else 1, (r + nr, c + nc, nd)) for nd, (nr, nc) in enumerate(md) if 0 <= r + nr < R and 0 <= c + nc < C and board[r + nr][c + nc] != '*' and (d + 2) % 4 != nd)

dist = [[[INF] * 4 for _ in range(C)] for _ in range(R)]
dist[sr][sc] = [0] * 4
q = deque((0, (sr+nr, sc+nc, i)) for i, (nr, nc) in enumerate(md) if 0 <= sr+nr < R and 0 <= sc+nc < C and board[sr+nr][sc+nc] != '*')

while q:
    cnt, (r, c, d) = q.popleft()
    if dist[r][c][d] <= cnt:
        continue
    dist[r][c][d] = cnt
    for ncnt, (nr, nc, nd) in next_i(r, c, d):
        if dist[nr][nc][nd] > cnt + ncnt:
            if ncnt == 0:
                q.appendleft((cnt, (nr, nc, nd)))
            else:
                q.append((cnt + 1, (nr, nc, nd)))

print(min(dist[er][ec]))