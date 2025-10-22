N, M = map(int, input().split())
trees = tuple(map(int, input().split()))

l, r = 0, max(trees)

while l <= r:
    m = (l + r) // 2
    amount = sum(max(0, t - m) for t in trees)
    if amount >= M:
        l = m + 1
    else:
        r = m - 1

print(r)