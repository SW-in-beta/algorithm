N = int(input())
l = list(map(int, input().split()))
i, j = 0, len(l) - 1
M, a, b = float('inf'), -1, -1

while i < j:
    m = l[i] + l[j]
    if abs(m) < M:
        M = abs(m)
        a = l[i]
        b = l[j]
    if m < 0:
        i += 1
    elif m > 0:
        j -= 1
    else:
        break

print(a, b)