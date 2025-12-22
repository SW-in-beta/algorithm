import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ants = []
for _ in range(N):
    ants.append(' '.join(input().split()[1:]))
    
ants.sort()

parent = []

for ant in ants:
    i = 0
    res = ant.split(' ')
    while i < len(parent) and i < len(res):
        if parent[i] != res[i]:
            break
        i += 1
    parent = parent[:i]
    for j in range(i, len(res)):
        print('--' * j + res[j])
        parent.append(res[j])