"""
분리집합. 이거 union find가 더 쉬울 것 같은데.
주어지는 입력이 뭐야.
n이 컴퓨터 개수이고, computers는 간선인데 배열로 나타나있다.
"""

def find(n, ps):
    if ps[n] != n:
        ps[n] = find(ps[n], ps)
    return ps[n]

def union(u, v, ps):
    pu = find(u, ps)
    pv = find(v, ps)
    if pu != pv:
        ps[pu] = pv
    
def solution(n, computers):
    ps = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j, ps)
    res = set()
    for i in range(n):
        res.add(find(i, ps))
    return len(res)