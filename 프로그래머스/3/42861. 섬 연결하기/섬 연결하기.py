"""
모든 섬이 서로 통행 가능하도록? 최소 신장 트리 아닌가 이거
최소 신장 트리가 그리디이긴 하지

union/find를 이용한 최소 신장트리로 가보자.
heap을 이용해서 간선을 하나씩 꺼낸다.
같은 부모가 아니라면 union.
같은 부모라면 패스
그러다가 전부 연결되면 끝

"""
from heapq import heappush, heappop

def find(u, parents):
    if parents[u] != u:
        parents[u] = find(parents[u], parents)
    return parents[u]

def union(u, v, parents):
    if u != v:
        parents[u] = v
        
def solution(n, costs):
    parents = [i for i in range(n)]
    costs = sorted([(w, u, v) for u, v, w in costs])
    total = 0
    for w, u, v in costs:
        pu = find(u, parents)
        pv = find(v, parents)
        if pu == pv:
            continue
        total += w
        union(pu, pv, parents)
        
    return total