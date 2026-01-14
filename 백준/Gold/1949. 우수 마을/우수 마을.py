import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
people = [0] + list(map(int, input().split()))
dp = [None] * (N+1)

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
        
def recur(u, parent=None):
    if dp[u] is not None:
        return dp[u]
    res = [people[u], 0, 0]
    gap = sys.maxsize
    cnt = 0
    for v in tree[u]:
        if v == parent:
            continue
        prior, non_and_non, non_and_prior = recur(v, u)
        res[0] += max(non_and_non, non_and_prior)
        res[1] += non_and_prior
        res[2] += max(prior, non_and_prior)
        if prior >= non_and_prior:
            cnt += 1
        else:
            gap = min(gap, non_and_prior - prior)
    
    if cnt == 0:
        res[2] -= gap
    dp[u] = res    
    return dp[u]

print(max(recur(1)))