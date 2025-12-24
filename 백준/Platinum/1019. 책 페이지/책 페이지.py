n = list(input())
prev = 0
count = [0] * 10
for i in range(len(n)):
    num = int(n[i])
    exp = 10 ** (len(n) - 1 - i)
    for j in range(10):
        count[j] += prev * exp
    for j in range(num):
        count[j] += exp
    count[num] += int(''.join(n[i+1:]) or '0') + 1
    prev *= 10
    prev += num
    
for i in range(len(n)):
    count[0] -= 10 ** i
    
print(*count)