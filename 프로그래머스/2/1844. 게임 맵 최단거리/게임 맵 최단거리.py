"""
백트래킹 느낌이 난다
일단 너비우선 탐색
visited가 있어야 하고

일단 재귀로 해보자.

지나다니면서 +1씩 업데이트해주기? 그보다 짧으면 패스하고.
일단 이렇게 하되 백트래킹도 공부해보자.
"""
from collections import deque

step = ((1, 0), (0, 1), (-1, 0), (0, -1))
def next_step(r, c, maps):
    return [(r+nr, c+nc) for nr, nc in step if 0 <= r+nr < len(maps) and 0 <= c+nc < len(maps[0]) and maps[r+nr][c+nc]]

INF = float('inf')

def solution(maps):
    maps = [[INF if e else 0 for e in row] for row in maps]
    q = deque([(0, 0, 1)])
    while q:
        r, c, cnt = q.popleft()
        if maps[r][c] <= cnt:
            continue
        maps[r][c] = cnt
        cnt += 1
        for nr, nc in next_step(r, c, maps):
            if maps[nr][nc] > cnt:
                q.append((nr, nc, cnt))
    res = maps[-1][-1]
    return res if res < INF else -1