import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(int(input()) for _ in range(N))
sums = set()

for i in range(N):
    for j in range(i, N):
        sums.add(nums[i] + nums[j])
        
for i in range(len(nums) - 1, -1, -1):
    k = nums[i]
    for j in range(i):
        z = nums[j]
        xy = k - z
        if xy in sums:
            print(k)
            exit()