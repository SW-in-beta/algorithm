import sys
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())
P = [i for i in range(V+1)]
def find(v):
    if P[v] != v:
        P[v] = find(P[v])
    return P[v]

def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return False
    P[pu] = P[pv]
    return True

h = []
for _ in range(E):
    a, b, c = map(int, input().split())
    h.append((c, a, b))

h.sort()
cost = 0
cnt = 0
i = 0
while i < len(h) and cnt < V - 1:
    c, a, b = h[i]
    if union(a, b):
        cnt += 1
        cost += c    
    i += 1

print(cost)