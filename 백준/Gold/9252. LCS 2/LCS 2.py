import sys
sys.setrecursionlimit(10**6)

s1 = input()
s2 = input()

lcs = [[None] * len(s2) for _ in s1]

def find_lcs(i, j):
    if i < 0 or j < 0:
        return ''
    if lcs[i][j] != None:
        return lcs[i][j]
    flag = s1[i] if s1[i] == s2[j] else ''
    if flag:
        base = find_lcs(i-1, j-1)
    else:
        left = find_lcs(i-1, j)
        right = find_lcs(i, j-1)
        base = left if len(left) >= len(right) else right
    lcs[i][j] = base + flag
    return lcs[i][j]
l = find_lcs(len(s1) - 1, len(s2) - 1)
print(len(l))
print(l)