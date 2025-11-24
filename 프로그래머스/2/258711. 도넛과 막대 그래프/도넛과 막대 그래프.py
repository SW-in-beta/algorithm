"""
도넛 그래프 : n개의 정점 n개의 간선. 그리고 정점마다 간선은 나가는 것 하나, 들어오는 것 하나.
막대 그래프 : n개의 정점 n-1개의 간선. 정점마다 간선은 나가는 것 하나, 들어오는 것 하나. 두개는 나가는 것 하나 또는 들어오는 것 하나. (노드가 하나일 때 제외)
8자 그래프 : 2n+1개 정점 2n+2개 간선. 정점마다 나가는 것 하나, 들어오는 것 하나, 하나만 나가는 것 둘, 들어오는 것 둘.
이 모든것의 사이즈가 n
+ 그리고 방향그래프다!
degree를 계산해두고 있으면 되겠다.

도넛 그래프, 막대 그래프, 8자 그래프가 있고, 노드를 생성한 후 이 모든 그래프들의 임의의 노드에 연결했다.
생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수 구하기.
"""
def is_bar(num, graph, degree, start=None):
    return degree[num] != 0 or len(graph[num]) == 0

def is_eight(num, graph, degree, start=None):
    return len(graph[num]) > 1

def is_donut(num, graph, degree, start):
    return num == start

def search_graph(num, graph, degree):
    start = num
    while True:
        if is_bar(num, graph, degree):
            return 1
        if is_eight(num, graph, degree):
            return 2
        num = graph[num][0]
        if is_donut(num, graph, degree, start):
            return 0
        
from collections import defaultdict
        
def solution(edges):
    degree = defaultdict(int)
    graph = defaultdict(list)
    
    for u, v in edges:
        degree[u] += 1
        degree[v] -= 1
        graph[u].append(v)
    
    added_node = None
    for k, d in degree.items():
        if d > 1:
            added_node = k
            break

    type_count = [0] * 3
    for num in graph[added_node]:
        degree[num] += 1
        type_count[search_graph(num, graph, degree)] += 1
        
    return [added_node, *type_count]