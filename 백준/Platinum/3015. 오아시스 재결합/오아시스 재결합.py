import sys
input = lambda: sys.stdin.readline().rstrip()
q = []
cnt = 0

for _ in range(int(input())):
    h = int(input())
    
    while q and q[-1][0] < h:
        _, q_cnt = q.pop()
        cnt += q_cnt
    
    if q and q[-1][0] == h:
        cnt += q[-1][1]
        q[-1][1] += 1
        if len(q) > 1:
            cnt += 1
        continue
    
    if q:
        cnt += 1
    q.append([h, 1])
    
print(cnt)