import sys
import math
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
arr = [0] * (N+1)
for i in range(1, N+1):
    arr[i] = int(input())

h = math.ceil(math.log2(N))
size = 1 << (h+1)
tree = [0] * size

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(node*2, start, mid, idx, diff)
    update(node*2+1, mid+1, end, idx, diff)

init(1, 1, N)

out = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(1, 1, N, b, diff)
    else:
        out.append(str(query(1, 1, N, b, c)))

print("\n".join(out))