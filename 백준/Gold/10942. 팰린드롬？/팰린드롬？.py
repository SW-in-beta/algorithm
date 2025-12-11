import sys
input = sys.stdin.readline
N = int(input())
P = [['0'] * N for _ in range(N)]
seq = list(map(int, input().split()))

for i in range(N):
    l = i
    r = i
    while l >= 0 and r < N:
        if seq[l] != seq[r]:
            break
        P[l][r] = '1'
        l -= 1
        r += 1
        
    l = i
    r = i + 1
    while l >= 0 and r < N:
        if seq[l] != seq[r]:
            break
        P[l][r] = '1'
        l -= 1
        r += 1

M = int(input())
for _ in range(M):
    l, r = map(int, input().split())
    print(P[l-1][r-1])