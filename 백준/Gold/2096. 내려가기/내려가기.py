import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
max_dp = [0] * 3
min_dp = [0] * 3

for _ in range(N):
    a, b, c = map(int, input().split())
    max_a, max_b, max_c = max_dp
    min_a, min_b, min_c = min_dp
    max_dp[0] = max(max_a, max_b) + a
    max_dp[1] = max(max_a, max_b, max_c) + b
    max_dp[2] = max(max_b, max_c) + c
    min_dp[0] = min(min_a, min_b) + a
    min_dp[1] = min(min_a, min_b, min_c) + b
    min_dp[2] = min(min_b, min_c) + c
    
print(max(max_dp), min(min_dp))