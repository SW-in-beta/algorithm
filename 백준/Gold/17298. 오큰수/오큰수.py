N = int(input())
answer = ['-1'] * N
stack = []

for i, e in enumerate(map(int, input().split())):
    while stack and stack[-1][1] < e:
        si, se = stack.pop()
        answer[si] = str(e)
    stack.append((i, e))

print(' '.join(answer))