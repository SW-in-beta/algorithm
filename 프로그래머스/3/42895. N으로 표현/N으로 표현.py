"""
DP의 작은 단위를 뭘로 해야할까.
number보다 더 큰수에서도 하나만 추가해서 number를 만들 수 있다. 이렇게되면 DP가 많이 어려워질듯
개수를 늘려가면서 하나하나 만들어보자.

1 - N
2 - NN, N*N, N/N, N+N, N-N(의미X)
3 - NN NN*N, NN/N, NN+N, NN-N, N*N*N, N*N/N 이것도 끝도 없을 것 같다.

최솟값이 8보다 크면 -1을 return 한다는게 핵심 -> 경우의 수를 다 구할 수 있지 않을까?
3을 구하려면, 1 2에 있었던 친구들을 더하거나 빼거나 나누거나 곱하거나. 그리고 NNN까지.
4일때는 1 3, 2 2를 하면 될듯

아아아아아아아아아아악
한 테스트가 뭘까
아 알겠다
"""
from operator import add, sub, mul, floordiv as div
from itertools import product

def solution(N, number):
    opers = [add, sub, mul, div]
    dp = [None] + [set([int(str(N) * i)]) for i in range(1, 9)]
    
    for i in range(1, 9):
        if number in dp[i]:
            return i
        for j in range(1, i // 2 + 1):
            k = i - j
            for p in product(dp[j], dp[k]):
                e1, e2 = sorted(p)
                for o in opers:
                    res = o(e2, e1)
                    if res == number:
                        return i
                    if res:
                        dp[i].add(res)    
    return -1