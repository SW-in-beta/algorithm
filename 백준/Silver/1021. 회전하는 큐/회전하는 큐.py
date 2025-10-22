from collections import deque

def move_left(dq):
    e = dq.popleft()
    dq.append(e)
    return dq

def move_right(dq):
    e = dq.pop()
    dq.appendleft(e)
    return dq

n, m = map(int, input().split())
l = map(int, input().split())
dq = deque(i + 1 for i in range(n))
c = 0
for i in l:
    left = dq.index(i)
    right = len(dq) - left
    if left <= right:
        c += left
        for _ in range(left):
            move_left(dq)
    else:
        c += right
        for _ in range(right):
            move_right(dq)
    dq.popleft()

print(c)