import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
seq = map(int, input().split())
P = [0]
for i in seq:
    P.append(P[-1] + i)

for _ in range(M):
    i, j = map(int, input().split())
    print(P[j] - P[i-1])