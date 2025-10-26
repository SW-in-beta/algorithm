import sys
input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())
p = [i for i in range(n+1)]

def find(n):
    if p[n] != n:
        p[n] = find(p[n])
    return p[n]

def union(u, v):
    pu = find(u)
    pv = find(v)
    p[pv] = pu
    
for _ in range(m):
    o, u, v = map(int, input().split())
    if o:
        print('YES' if find(u) == find(v) else 'NO')
    else: 
        union(u, v)