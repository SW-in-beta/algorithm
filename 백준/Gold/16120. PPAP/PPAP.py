S = input()
res = []
for i in range(len(S)):
    if S[i] == 'P':
        res.append(S[i])
        continue
    if len(res) < 2 or i == len(S) - 1:
        print('NP')
        exit()
    if not(res[-1] == 'P' and res[-2] == 'P' and S[i+1] == 'P'):
        print('NP')
        exit()
    res.pop()
    res.pop()

print('PPAP' if len(res) == 1 else 'NP')