L = int(input())
ad = input()

pi = [0] * L
i = 0
for j in range(1, L):
    while i > 0 and ad[i] != ad[j]:
        i = pi[i-1]
    if ad[i] == ad[j]:
        i += 1
        pi[j] = i

print(L - pi[-1])