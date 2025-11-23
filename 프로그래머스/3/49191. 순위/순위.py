"""
탐색을 한다고 했을 때, 어떤 경우에 순위를 매길 수 있고 어떤 경우에 매길 수 없나
이기는 방향으로 그래프를 그렸다고 생각해보자.
한줄로 쭈욱 있으면 가능.
아니다 그런 개념이 아님 애초에.
순위 결정 조건(from GPT) 모든 상대에 대해 이길 수 있냐 없냐가 결정되면 된다.
"""

def solution(n, results):
    win = [[False] * (n+1) for _ in range(n+1)]
    lose = [[False] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        win[i][i] = True
        lose[i][i] = True
        
    for a, b in results:
        win[a][b] = True
        lose[b][a] = True
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                win[i][j] = win[i][j] or (win[i][k] and win[k][j])
                lose[i][j] = lose[i][j] or (lose[i][k] and lose[k][j])
    return sum(1 if (sum(map(int, win[i])) + sum(map(int, lose[i])) - 2) == n-1 else 0 for i in range(1, n+1))
    