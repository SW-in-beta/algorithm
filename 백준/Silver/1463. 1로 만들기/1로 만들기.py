n = int(input())
d = [0, 0, 1, 1]
for i in range(4, n+1):
    ars = [i - 1]
    if i % 2 == 0: ars.append(i // 2)
    if i % 3 == 0: ars.append(i // 3)
    d.append(min(d[a] for a in ars)+1)

print(d[n])