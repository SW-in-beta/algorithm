from itertools import combinations

N, S = map(int, input().split())
seq = tuple(map(int, input().split()))
coms = [combinations(seq, i) for i in range(1, len(seq) + 1)]
print(sum(sum(1 if sum(c) == S else 0 for c in com) for com in coms))