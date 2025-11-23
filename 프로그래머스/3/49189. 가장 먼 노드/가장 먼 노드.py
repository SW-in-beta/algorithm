"""
1번 노드에서부터 최단 경로 다 구해야하네
1번부터 시작해서 bfs로 탐색. weight가 없다.
bfs
총 1개 이상 50,000개 이하의 간선.
"""
from collections import deque, Counter
INF = float('inf')

def solution(n, edge):
    dists = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    max_dist = 0
    q = deque([(1, 0)])
    while q:
        u, dist = q.popleft()
        if dists[u] <= dist:
            continue
        dists[u] = dist
        max_dist = max(max_dist, dist)
        dist += 1
        for v in graph[u]:
            if dists[v] > dist:
                q.append((v, dist))
    
    return Counter(dists)[max_dist]