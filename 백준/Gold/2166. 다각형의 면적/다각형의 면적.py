xs = []
ys = []
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

res = 0
for i in range(N):
    res += xs[i] * ys[(i + 1) % N]
    res -= ys[i] * xs[(i + 1) % N]

print(round(abs(res) / 2, 1))