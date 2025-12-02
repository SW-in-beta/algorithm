"""
번호가 있고, 출입구 쉼터 산봉우리가 있다.
양방향 통행 가능
쉼터 또는 산봉우리를 방문할 때마다 휴식 가능. intensity? -> 가장 큰 가중치

지점 수 n, 등산로 정보 paths, 출입구 gates, 산봉우리 summits.
n 50,000
paths 200,000
전부다 gates일수도 있네
summits 일수도 있고

어느 게이트를 가느냐는 중요하지 않다.
산봉우리에서 출발해서 계속 작은 간선들만 추가하다가, gate를 발견하면 끝나는거. 그게 해당 산봉우리를 가는 최소 intensity 루트.
visited를 관리하면서 heap에 웨이트들을 넣어주자.
"""
from heapq import heappush, heappop

def search(s, graph, gates, summits, min_intensity):
    visited = [False] * len(graph)
    intensity = 0
    h = []
    heappush(h, (0, s))
    
    while h:
        w, s = heappop(h)
        if visited[s]:
            continue
        visited[s] = True
        
        intensity = max(intensity, w)
        if s in gates:
            return intensity
        
        for ns, nw in graph[s]:
            if not visited[ns] and ns not in summits and nw <= min_intensity:
                heappush(h, (nw, ns))
    return min_intensity + 1
    

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))
    gates = set(gates)
    summits = set(summits)
    
    min_intensity = 10 ** 7 + 1
    min_summit = n+1
    for summit in summits:
        intensity = search(summit, graph, gates, summits, min_intensity)
        if intensity > min_intensity:
            continue
        if intensity < min_intensity:
            min_summit = summit
            min_intensity = intensity
            continue
        if intensity == min_intensity:
            min_summit = min(min_summit, summit)
            continue
        
    return [min_summit, min_intensity]