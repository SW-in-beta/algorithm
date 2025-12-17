import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
A, B, C, D = [None] * n, [None] * n, [None] * n, [None] * n

for i in range(n):
    a, b, c, d = map(int, input().split())
    A[i], B[i], C[i], D[i] = a, b, c, d

case = Counter(C[i] + D[j] for i in range(n) for j in range(n))

answer = 0

for i in range(n):
    for j in range(n):
        answer += case[-(A[i] + B[j])]

print(answer)