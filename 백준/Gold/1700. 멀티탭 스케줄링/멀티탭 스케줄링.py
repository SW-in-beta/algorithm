from collections import deque

N, K = map(int, input().split())
next_turn = [deque() for _ in range(K+1)]
seq = list(map(int, input().split()))
for i, e in enumerate(seq):
    next_turn[e].append(i)

cnt = 0
multitab = set()
for e in seq:
    next_turn[e].popleft()
    if len(multitab) < N:
        multitab.add(e)
        continue
    if e in multitab:
        continue

    cnt += 1

    cur = 0
    target = 0

    for m in multitab:
        if next_turn[m]:
            if next_turn[m][0] < cur:
                continue
            cur = next_turn[m][0]
            target = m
        else:
            target = m
            break 
    multitab.remove(target)
    multitab.add(e)

print(cnt)