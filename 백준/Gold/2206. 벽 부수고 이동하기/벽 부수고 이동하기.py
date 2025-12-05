import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
coord = ((0, 1), (0, -1), (1, 0), (-1, 0))
def next_coord(r, c):
    return [(r + nr, c + nc) for nr, nc in coord if 0 <= r + nr < N and 0 <= c + nc < M]

q = deque([(0, 0, 1, 1)])
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

while q:
    r, c, cnt, wall = q.popleft()
    if visited[r][c][wall]:
        continue
    visited[r][c][wall] = True
    if r == N-1 and c == M-1:
        print(cnt)
        exit()
    
    cnt += 1
    for nr, nc in next_coord(r, c):
        if board[nr][nc] == '1' and wall > 0 and not visited[nr][nc][0]:
            q.append((nr, nc, cnt, wall - 1))
            continue
        if board[nr][nc] == '0' and not visited[nr][nc][wall]:
            q.append((nr, nc, cnt, wall))

print(-1)