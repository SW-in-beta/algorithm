import sys
sys.setrecursionlimit(1000000)
input = lambda : sys.stdin.readline().rstrip()

def find_top(n, setlist):
  if setlist[n] != n:
    setlist[n] = find_top(setlist[n], setlist)
  return setlist[n]

def union_set(n1, n2, setlist):
  t1 = find_top(n1, setlist)
  t2 = find_top(n2, setlist)
  setlist[t1] = t2

def in_same_set(n1, n2, setlist):
  t1 = find_top(n1, setlist)
  t2 = find_top(n2, setlist)
  return t1 == t2

if __name__ == '__main__':
  n, m = map(int, input().split())
  setlist = [i for i in range(n+1)]
  for _ in range(m):
    com, n1, n2 = map(int, input().split())
    if com == 0:
      union_set(n1, n2, setlist)
    elif com == 1:
      print('YES' if in_same_set(n1, n2, setlist) else 'NO')