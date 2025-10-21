"""
사탕의 색이 다른 인접한 두 칸.
N*N이고 N <= 50 -> 전체 탐방할 수 있을듯
최대개수 어떻게 구하지? -> 다른 색을 바꾸는거니까, 같은 방향으로는 절대 안될 것
전체중에서 가장 긴 것들이 있을건데, 경우의 수는 그 가장 긴 것이 제일 길거나, 하나 짧거나, 아니다 이건 너무 많다.
그냥 전체를 고려하자.

1. 우 / 하로만 교대하면 된다
2. 교대 후에는 가로 세로 개수 세기
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(input()) for _ in range(N)]

dx = (1, 0)
dy = (0, 1) 

def swap(r, c, dir):
    board[r][c], board[r + dx[dir]][c + dy[dir]] = board[r + dx[dir]][c + dy[dir]], board[r][c]
    
def max_count(row):
    cur_max_cnt = 1
    prev = row[0]
    cnt = 1
    for e in row[1:]:
        if prev == e:
            cnt += 1
        else:
            cur_max_cnt = max(cur_max_cnt, cnt)
            prev = e
            cnt = 1
    return max(cur_max_cnt, cnt)

max_cnt = 1
for r in range(N-1):
    for c in range(N):
        swap(r, c, 0)
        max_cnt = max(max_cnt, max_count(board[r]), max_count(board[r+1]), max_count([row[c] for row in board]))
        swap(r, c, 0)

for r in range(N):
    for c in range(N-1):
        swap(r, c, 1)
        max_cnt = max(max_cnt, max_count(board[r]), max_count([row[c] for row in board]), max_count([row[c+1] for row in board]))
        swap(r, c, 1)
        
print(max_cnt)