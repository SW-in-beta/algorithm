import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parents = [i for i in range(N + 1)]

def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]
    
def union(u, v):
    u_parent = find(u)
    v_parent = find(v)
    parents[max(u_parent, v_parent)] = min(u_parent, v_parent)
    
for _ in range(M):
    union(*map(int, input().split()))
    
roots = set()
for i in range(1, N+1):
    roots.add(find(i))

print(len(roots))