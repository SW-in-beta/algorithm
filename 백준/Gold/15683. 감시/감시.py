import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []
CCTV = []
floor = N * M

for r in range(N):
    board.append([])
    for c, e in enumerate(map(int, input().split())):
        if e == 6:
            board[r].append(-1)
            floor -= 1
            continue
        elif e > 0:
            floor -= 1
            CCTV.append((r, c, e-1))
            board[r].append(1)
        else:
            board[r].append(0)

d = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def turnon(r, c, drt):
    dr, dc = d[drt]
    nr, nc = r + dr, c + dc
    cnt = 0
    while 0 <= nr < N and 0 <= nc < M:
        if board[nr][nc] == -1:
            break
        if board[nr][nc] == 0:
            cnt += 1
        board[nr][nc] += 1
        nr += dr
        nc += dc
    return cnt
        
def turnoff(r, c, drt):
    dr, dc = d[drt]
    nr, nc = r + dr, c + dc
    cnt = 0
    while 0 <= nr < N and 0 <= nc < M:
        if board[nr][nc] == -1:
            break
        board[nr][nc] -= 1
        if board[nr][nc] == 0:
            cnt += 1
        nr += dr
        nc += dc
    return cnt

directions = [[[i] for i in range(4)], [[0, 2], [1, 3]], [[i, (i+1) % 4] for i in range(4)], [[i, (i+1) % 4, (i+2) % 4] for i in range(4)], [[0, 1, 2, 3]]]

def detect(cctv_num):
    if cctv_num >= len(CCTV):
        return 0
    r, c, e = CCTV[cctv_num]
    max_cnt = 0
    for direction in directions[e]:
        cnt = 0
        for drt in direction:
            cnt += turnon(r, c, drt)
        cnt += detect(cctv_num + 1)
        max_cnt = max(max_cnt, cnt)
        for drt in direction:
            cnt -= turnoff(r, c, drt)
    return max_cnt

print(max(0, floor - detect(0)))