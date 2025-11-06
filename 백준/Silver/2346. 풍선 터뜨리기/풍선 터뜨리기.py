N = int(input())
seq = list(enumerate(map(int, input().split())))
res = []
i = 0
while True:
    n, s = seq.pop(i)
    res.append(n+1)
    if not seq: break
    i = (i + (s - 1 if s > 0 else s)) % len(seq)

print(' '.join(map(str, res)))