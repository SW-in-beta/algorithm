stack = []
cnt = 0

for i, e in enumerate(input()):
    if e == '(':
        stack.append((e, i))
        continue
    pe, pi = stack.pop()
    cnt += len(stack) if pi == i - 1 else 1

print(cnt)