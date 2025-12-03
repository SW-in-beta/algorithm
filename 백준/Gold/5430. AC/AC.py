import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

answer = []
for _ in range(T):
    cnt = [0, 0]
    p = input().split('R')
    n = int(input())
    arr = input().strip('[]').split(',')
    arr = [a for a in arr if a]

    for i, d in enumerate(p):
        cnt[i % 2] += len(d)

    if sum(cnt) > len(arr):
        answer.append("error")
    else:
        res = arr[cnt[0]:len(arr)-cnt[1]]
        res = res if len(p) % 2 else list(reversed(res))
        answer.append("[" + ','.join(res) + "]")

print('\n'.join(answer))