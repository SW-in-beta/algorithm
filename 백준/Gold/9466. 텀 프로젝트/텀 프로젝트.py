import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    answer = 0
    
    for i in range(1, n+1):
        cur = i
        stack = []
        cur_set = set()
        
        while True:
            if cur in cur_set:
                while True:
                    prev = stack.pop()
                    if prev == cur:
                        break
                answer += len(stack)
                break
            
            if visited[cur]:
                answer += len(stack)
                break
            
            visited[cur] = True
            cur_set.add(cur)
            stack.append(cur)
            cur = graph[cur]
    
    print(answer)