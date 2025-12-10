N, S = map(int, input().split())
seq = list(map(int, input().split()))

i = 0
j = 0
s = seq[0]
length = N + 1

while True:
    if s < S:
        j += 1
        if j == N:
            break
        s += seq[j]
    else:
        length = min(length, j - i + 1)
        s -= seq[i]
        i += 1
        if i > j:
            break

print(length if length <= N else 0)    