import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_time(n, graph, D, times):
    if times[n] == -1:
        if len(graph[n]) == 0:
            times[n] = D[n]
        else:
            times[n] = max(get_time(m, graph, D, times) for m in graph[n]) + D[n]
    return times[n]


for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    times = [-1] * (N + 1)
    for _ in range(K):
        n, m = map(int, input().split())
        graph[m].append(n)
    print(get_time(int(input()), graph, D, times))