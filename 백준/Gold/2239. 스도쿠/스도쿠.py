import sys
input = lambda: sys.stdin.readline().rstrip()

squares = [[0] * 3 for _ in range(3)]
rows = [0] * 9
cols = [0] * 9

def possible_nums(r, c):
    res = squares[r // 3][c // 3] | rows[r] | cols[c]
    return [i for i, s in enumerate(reversed(bin(res)[2:-1].zfill(9)), start = 1) if s == '0']
        
def append_num(r, c, num):
    board[r][c] = num
    res = 1 << num
    rows[r] |= res
    cols[c] |= res
    squares[r // 3][c // 3] |= res

def remove_num(r, c, num):
    board[r][c] = 0
    res = 2 ** 11 - 1 - (1 << num)
    rows[r] &= res
    cols[c] &= res
    squares[r // 3][c // 3] &= res


board = [[0] * 9 for _ in range(9)]    
empty = []
for r in range(9):
    for c, s in enumerate(input()):
        board[r][c] = s
        s = int(s)
        append_num(r, c, s)
        if s == 0:
            empty.append((r, c))
empty = list(reversed(empty))

def find_answer():
    if not empty:
        return True
    
    r, c = empty.pop()
    possible = possible_nums(r, c)
    
    for num in possible:
        append_num(r, c, num)
        res = find_answer()
        if res:
            return True
        remove_num(r, c, num)
        
    empty.append((r, c))
    return False

find_answer()
print('\n'.join(''.join(map(str, row)) for row in board))