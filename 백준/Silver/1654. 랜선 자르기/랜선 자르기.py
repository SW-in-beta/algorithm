import sys
input = lambda: sys.stdin.readline().rstrip()

def get_sum(length, LAN):
    return sum(l // length for l in LAN)

K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]
length = max(LAN) * 2
start, end = 1, length
while start <= end:
    mid = (start + end) // 2
    sum_length = get_sum(mid, LAN)
    if sum_length >= N:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)