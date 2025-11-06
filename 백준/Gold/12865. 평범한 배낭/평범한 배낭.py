import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
max_values = [0] * (K+1)

for w, v in items:
    for i in range(K, w-1, -1):
        max_values[i] = max(max_values[i], max_values[i-w] + v)
print(max_values[K])