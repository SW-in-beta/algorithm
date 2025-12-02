import sys
input = lambda: sys.stdin.readline().rstrip()

stack = []
cnt = 0
for _ in range(int(input())):
    h = int(input())
    while stack and stack[-1] <= h:
        stack.pop()
    cnt += len(stack)
    stack.append(h)
print(cnt)