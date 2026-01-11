import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parents = [i for i in range(N+1)]

def find(u):
    if parents[u] != u:
        parents[u] = find(parents[u])
    return parents[u]

def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return False
    parents[pu] = pv
    return True

cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    res = union(u, v)
    cnt += 0 if res else 1
    
for u in range(1, N+1):
    find(u)

cnt += len(set(parents)) - 2

print(cnt)