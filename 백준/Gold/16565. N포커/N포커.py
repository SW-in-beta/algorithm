from math import comb
n = int(input())
cnt = 0
for i in range(1, n // 4 + 1):
    c = comb(13, i) * comb(52 - 4 * i, n - 4 * i)
    if i % 2:
        cnt += c
    else:
        cnt -= c
    cnt %= 10007
print(cnt)