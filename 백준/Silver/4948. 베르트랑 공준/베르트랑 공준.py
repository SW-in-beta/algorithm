import sys
input = lambda: sys.stdin.readline().rstrip()
n = 123456
max_n = 2 * n
a = [0] * (max_n + 1)
prime = [True] * (max_n + 1)
prime[1] = False

for i in range(2, max_n + 1):
    a[i] = a[i-1]
    if prime[i]:
        a[i] += 1
        for j in range(i*i, max_n + 1, i):
            prime[j] = False

while (s := int(input())) > 0:
    print(a[2 * s] - a[s])