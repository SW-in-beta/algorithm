import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def find_idxs(r, c):
    idxs = [(r+dr, c+dc) for dr, dc in move]
    filtered_idxs = [(nr, nc) for nr, nc in idxs if 0 <= nr < 6 and 0 <= nc < len(board[nr])]
    return filtered_idxs

def find_bomb(board):
    visited = [[False] * 12 for _ in range(6)]
    bombs = []
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            bomb = []
            q = deque([(r, c)])
            while q:
                nr, nc = q.popleft()
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                bomb.append((nr, nc))
                idxs = find_idxs(nr, nc)
                filtered_idxs = [(cr, cc) for cr, cc in idxs if board[cr][cc] == col and not visited[cr][cc]]
                q.extend(filtered_idxs)
            if len(bomb) >= 4:
                bombs.append(bomb)
    return bombs

board = [list(input()) for _ in range(12)]
board = [list(filter(lambda x: x != '.', reversed(element))) for element in zip(*board)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 0
while True:
    bombs = find_bomb(board)
    if not bombs:
        break
    cnt += 1
    for bomb in bombs:
        for r, c in bomb:
            board[r][c] = '.'
    board = [list(filter(lambda x: x != '.', row)) for row in board]
    
print(cnt)