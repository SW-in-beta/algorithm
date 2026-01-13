import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

V = int(input())
trees = [[] for _ in range(V+1)]
max_len = 0
max_u = 0
for _ in range(V):
    info = tuple(map(int, input().split()))
    u = info[0]
    for i in range(1, len(info) - 1, 2):
        trees[u].append((info[i], info[i+1]))
    if len(trees[u]) > max_len:
        max_len = len(trees[u])
        max_u = u
        
def recur(u, parent=None):
    max_to_leaf, second_to_leaf, max_in_tree = 0, 0, 0
    for v, c in trees[u]:
        if v == parent:
            continue
        local_to_leaf, local_in_tree = recur(v, u)
        local_to_leaf += c
        if local_to_leaf > max_to_leaf:
            second_to_leaf = max_to_leaf
            max_to_leaf = local_to_leaf
        elif local_to_leaf > second_to_leaf:
            second_to_leaf = local_to_leaf
        max_in_tree = max(max_in_tree, local_in_tree)
    if second_to_leaf > 0:
        max_in_tree = max(max_in_tree, max_to_leaf + second_to_leaf)
    max_in_tree = max(max_in_tree, max_to_leaf)
    return max_to_leaf, max_in_tree

print(recur(max_u)[1])