import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    seq = sorted([input() for _ in range(n)])
    c = seq[0]
    ans = 'YES'
    for s in seq[1:]:
        if len(s) > len(c) and s[:len(c)-len(s)] == c:
            ans = 'NO'
            break
        c = s
    print(ans)