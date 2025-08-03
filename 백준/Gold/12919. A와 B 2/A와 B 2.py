S = input()
T = input()

def dfs(T):
    if len(T) == len(S):
        if S == T:
            print(1)
            exit()
        else:
            return 0

    if T[-1] == 'A':
        dfs(T[:-1])

    if T[0] == 'B':
        dfs(T[::-1][:-1])

dfs(T)
print(0)