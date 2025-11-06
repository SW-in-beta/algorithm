import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    stack = []
    for s in input():
        if s == '(':
            stack.append(s)
        else:
            try:
                stack.pop()
            except:
                stack.append('(')
                break
    print('NO' if stack else 'YES')