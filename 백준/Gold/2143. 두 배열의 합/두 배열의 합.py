import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sum = [0] + list(A)
B_sum = [0] + list(B)

for i in range(1, n+1):
    A_sum[i] += A_sum[i-1]
    
for i in range(1, m+1):
    B_sum[i] += B_sum[i-1]
    
def get_part_sum(i, j, target_sum):
    return target_sum[j] - target_sum[i-1]

A_counter = Counter(get_part_sum(i, j, A_sum) for i in range(1, n+1) for j in range(i, n+1))
B_counter = Counter(get_part_sum(i, j, B_sum) for i in range(1, m+1) for j in range(i, m+1))

answer = 0
for k, v in A_counter.items():
    answer += v * B_counter[T - k]

print(answer)