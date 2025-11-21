"""
DP 느낌인데 -> X

테이블의 퍼즐 조각을 게임 보드의 빈 공간에 올려 놓기
조각은 한 번에 하나씩
회전 가능. 뒤집을수는 없음.

테이블에 존재하는 퍼즐 조각은 전부 인접하지 않는다.

게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안된다? -> 이 조건 덕분에 들어가는 순서가 중요하진 않다.
그럼 테이블의 퍼즐 조각을 옮겼을 때도 이미 채워져 있어야하나? -> 그치 무조건 딱 맞는 곳에 들어가야 한다. ㅇㅋ 이건 괜찮
결국 들어갈 수 있는 자리를 어떻게 찾을지가 중요하네

빈공간을 어떻게 찾을지
그리고 테이블의 블록 모양은 어떻게 파악할지
마지막으로 그 공간들을 어떻게 매핑할지 -> 회전까지 고려해야해서 살짝 빡세다

공간 찾는 건 탐색하면 될 것 같다.
블록 모양도.
근데 이걸 어떻게 계산해서 비교할지가 관건

빈 공간이 갖고 있어야할 요소를 생각해보자. 위치는 필요없네
1. 빈 공간의 크기 -> 이게 매칭이 안되면 검사할 필요가 없다.
2. 회전 시켰을 때 매칭이 됐냐가 중요한데, r, c길이를 확인하는건가
3. 어떤 규칙에 따라 미리 회전시켜두면 될 것 같은데. -> 그냥 회전 시키는걸로 하자

아 진짜 풀기 싫은 문제다.

1. 블록 찾기 구현
table은 1, game_board는 0으로 찾아가기. 탐색을 하면서 lxrytxby를 구해서 그부분만 슬라이싱 후 저장

2. 회전 구현
3. 같은지 확인하기 구현
"""
from collections import deque

d = ((0, 1), (1, 0), (0, -1), (-1, 0))
def next_idx(r, c, board):
    n = [(r+dr, c+dc) for dr, dc in d]
    return [(nr, nc) for nr, nc in n if 0 <= nr < len(board) and 0 <= nc < len(board)]

def find_block(board, target=1):
    blocks = []
    visited = set()
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != target or (r, c) in visited:
                continue
            lr, rr, tc, bc = r, r, c, c
            q = deque([(r, c)])
            cnt = 0
            while q:
                nr, nc = q.popleft()
                if (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                cnt += 1
                lr = min(lr, nr)
                rr = max(rr, nr)
                tc = min(tc, nc)
                bc = max(bc, nc)
                for nnr, nnc in next_idx(nr, nc, board):
                    if board[nnr][nnc] == target and (nnr, nnc) not in visited:
                        q.append((nnr, nnc))
            blocks.append(([row[tc:bc+1] for row in board[lr:rr+1]], cnt))
    return blocks

def rotate(block):
    return [[row[i] for row in block] for i in range(len(block[0])-1, -1, -1)]

def same_block(block1, block2):
    for i in range(4):
        if block1 == block2:
            return True
        block2 = rotate(block2)
    return False
            
def solution(game_board, table):
    board_blocks = find_block(game_board, 0)
    table_blocks = find_block(table, 1)
    for block, _ in table_blocks:
        for r in range(len(block)):
            for c in range(len(block[0])):
                block[r][c] = (block[r][c] + 1) % 2
    visited = set()
    for b_block, b_cnt in board_blocks:
        for i, [t_block, t_cnt] in enumerate(table_blocks):
            if i in visited:
                continue
            res = same_block(b_block, t_block)
            if not res:
                continue
            print(b_block, t_block, t_cnt)
            visited.add(i)
            break

    return sum(table_blocks[i][1] for i in visited)