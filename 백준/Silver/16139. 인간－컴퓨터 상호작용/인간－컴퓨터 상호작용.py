from bisect import bisect_left, bisect_right
import sys
input = lambda : sys.stdin.readline().rstrip()

alphabets = [[] for _ in range(ord('z') - ord('a') + 1)]
string = input()

for i, s in enumerate(string):
    alphabets[ord(s) - ord('a')].append(i)
    
q = int(input())
for _ in range(q):
    a, l, r = input().split()
    alphabet = alphabets[ord(a) - ord('a')]
    index_l = bisect_left(alphabet, int(l))
    index_r = bisect_right(alphabet, int(r))
    print(index_r - index_l)