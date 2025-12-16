from bisect import bisect_left as bisect

N = int(input())
liquids = sorted(map(int, input().split()))

gap = float('inf')
ls = None

for i in range(N):
    for j in range(i+1, N):
        target = -(liquids[i] + liquids[j])
        k = bisect(liquids, target)
        r = k
        l = k - 1
        while r == i or r == j:
            r += 1
        while l == i or l == j:
            l -= 1
            
        if r < N:
            candidate = liquids[i] + liquids[j] + liquids[r]
            if gap > abs(candidate):
                gap = abs(candidate)
                ls = (liquids[i], liquids[j], liquids[r])
        if l >= 0:
            candidate = liquids[i] + liquids[j] + liquids[l]
            if gap > abs(candidate):
                gap = abs(candidate)
                ls = (liquids[i], liquids[j], liquids[l])
                
print(' '.join(map(str, sorted(ls))))