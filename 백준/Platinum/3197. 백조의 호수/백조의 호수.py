import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
gid = lambda r, c : r * C + c

l = tuple(tuple(input()) for _ in range(R))
p = [gid(r, c) for r in range(R) for c in range(C) ]
rk = [0] * (gid(R-1, C-1) + 1)
ds = [float('inf')] * (gid(R-1, C-1) + 1)

d = ((0, 1), (1, 0), (-1, 0), (0, -1))
def ni(r, c):
    return [(r+dr, c+dc) for dr, dc in d if 0 <= r + dr < R and 0 <= c + dc < C]

def find(id):
    while p[id] != id:
        p[id] = p[p[id]]
        id = p[id]
    return p[id]

def union(id1, id2):
    p1 = find(id1)
    p2 = find(id2)
    rk1 = rk[p1]
    rk2 = rk[p2]

    if p1 == p2: return
    if rk1 <= rk2:
        p[p1] = p2
        if rk1 == rk2:
            rk[p2] += 1
    else:
        p[p2] = p1

s = []
q = deque([])
for r in range(R):
    for c in range(C):
        id = gid(r, c)
        if l[r][c] == 'X':
            continue
        q.append((r, c))
        ds[id] = 0
        if l[r][c] == 'L':
            s.append(id)

p_day = 0

while q:
    r, c = q.popleft()
    id = gid(r, c)
    day = ds[id]
    if p_day < day:
        if find(s[0]) == find(s[1]):
            break
        p_day = day
    
    for nr, nc in ni(r, c):
        nid = gid(nr, nc)
        if ds[nid] <= day:
            union(id, nid)
        elif ds[nid] == float('inf'):
            ds[nid] = day + 1
            q.append((nr, nc))

print(p_day)