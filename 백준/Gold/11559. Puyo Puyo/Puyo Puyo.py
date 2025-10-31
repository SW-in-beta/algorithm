import sys
input = lambda : sys.stdin.readline().rstrip()

board = [[] for _ in range(6)]
for j in range(-1, -13, -1):
    for i, e in enumerate(input()):
        if e != '.':
            board[i] = [e] + board[i]
        

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

def next_index(i, j):
    return ((i + nx, j + ny) for nx, ny in zip(dx, dy) if 0 <= i + nx < 6 and 0 <= j + ny < len(board[i + nx]))

def bomb(board):
    bombs = []
    visited = [[False] * len(row) for row in board]
    for i in range(6):
        for j in range(len(board[i])):
            if visited[i][j]: continue
            color = board[i][j]
            b = []
            q = [(i, j)]
            while q:
                r, c = q.pop()
                if visited[r][c]: continue
                visited[r][c] = True
                b.append((r, c))
                for nr, nc in next_index(r, c):
                    if not visited[nr][nc] and board[nr][nc] == color:
                        q.append((nr, nc))
            if len(b) >= 4: bombs.append(b)
    return bombs

def remove(bombs, board):
    for b in bombs:
        for r, c in b:
            board[r][c] = '.'
    return [list(filter(lambda x: x != '.', row)) for row in board]

cnt = 0
while True:
    bombs = bomb(board)
    if not bombs:
        break
    cnt += 1
    board = remove(bombs, board)
    
print(cnt)