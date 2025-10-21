N = int(input())
res = [0] * (N+1)
for i in range(2, N+1):
    cur_res = res[i-1]
    if i % 2 == 0:
        cur_res = min(cur_res, res[i // 2])
    if i % 3 == 0:
        cur_res = min(cur_res, res[i // 3])
    res[i] = cur_res + 1

print(res[N])