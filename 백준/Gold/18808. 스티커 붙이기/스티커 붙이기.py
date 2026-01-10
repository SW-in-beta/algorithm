import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int ,input().split())

def rotate_sticker(sticker):
    return [[sticker[c][r] for c in range(len(sticker)-1, -1, -1)] for r in range(len(sticker[0]))]
    
def sticker_to_bin(sticker):
    result = []
    for row in sticker:
        res = 0
        for col in row:
            res = res << 1
            res += int(col)
        result.append(res)
    return result

def put_sticker(board, sticker, cnt):
    SR, SC = len(sticker), len(sticker[0])
    binned_sticker = sticker_to_bin(sticker)
    
    for r in range(N - SR + 1):
        for c in range(M - SC + 1):
            flag = True
            for i in range(SR):
                b = board[r + i]
                s = binned_sticker[i]
                s <<= M - SC - c
                if b & s:
                    flag = False
                    break
            if flag:
                for i in range(SR):
                    s = binned_sticker[i]
                    s <<= M - SC - c
                    board[r + i] |= s
                return cnt
    return 0

board = [0] * N
total = 0

for _ in range(K):
    r, c = map(int, input().split())
    sticker = []
    cnt = 0
    for _ in range(r):
        sticker.append([])
        for s in input().split():
            cnt += int(s)
            sticker[-1].append(s)
    
    for l in range(4):
        res = put_sticker(board, sticker, cnt)
        if res > 0:
            total += res
            break
        sticker = rotate_sticker(sticker)

print(total)