"""
아이디어가 대박이네
두배로 늘려서 진행하면 된다...그러면 이동했을 때 선분으로 갈 일이 없다.
와
내부영역은 imos로 가볼까
외부영역만 
""" 
from collections import deque
def solution(rectangle, *arg):
    cX, cY, iX, iY = map(lambda x: x * 2, arg)
    rectangle = [tuple(e * 2 for e in rect) for rect in rectangle]
    board = [[0] * 102 for _ in range(102)]
    for lx, ty, rx, by in rectangle:
        board[lx+1][ty+1] -= 100
        board[lx+1][by] += 100
        board[rx][ty+1] += 100
        board[rx][by] -= 100
        # 선도 여기서 그어버리자. 가로선부터
        board[lx][ty] += 1
        board[rx+1][ty] -= 1
        board[lx][ty+1] -= 1
        board[rx+1][ty+1] += 1
        board[lx][by] += 1
        board[rx+1][by] -= 1
        board[lx][by+1] -= 1
        board[rx+1][by+1] += 1
        # 세로선
        board[lx][ty] += 1
        board[lx][by+1] -= 1
        board[lx+1][ty] -= 1
        board[lx+1][by+1] += 1
        board[rx][ty] += 1
        board[rx][by+1] -= 1
        board[rx+1][ty] -= 1
        board[rx+1][by+1] += 1
        
    # 가로로 합구하기
    for r in range(102):
        for c in range(1, 102):
            board[r][c] += board[r][c-1]
    # 세로로 합 구하기
    for r in range(1, 102):
        for c in range(102):
            board[r][c] += board[r-1][c]
    
    d = ((0, 1), (1, 0), (0, -1), (-1, 0))
    INF = float('inf')
    cnts = [[INF] * 102 for _ in range(102)]
    q = deque([(cX, cY, 0)])
    
    while q:
        x, y, cnt = q.popleft()
        if x == iX and y == iY:
            return cnt // 2
        cnts[x][y] = cnt
        cnt += 1
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if board[nx][ny] > 0 and cnts[nx][ny] > cnt:
                q.append((nx, ny, cnt))