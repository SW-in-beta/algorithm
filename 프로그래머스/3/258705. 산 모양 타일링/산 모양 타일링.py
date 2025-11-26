"""
모든 경우의 수를 구해야한다.
마름모의 개수를 늘려가면서 구하면 될 것 같은데, 마름모의 위치를 어떻게 잡으면 좋을까.

1 <= n <= 100,000
top이 있냐 없냐에 따라 나뉠 것 같다.

규칙이 있지 않을까. 갖다 이어붙이는 것 뿐인데.
한 삼각형이 갖는 경우의 수? 그래프?

그래프 탐색이라기엔 노드가 너무 많다. 뭔가 규칙이 있을 것 같은데

제일 오른쪽의 삼각형을 칠한 경우와 칠하지 않은 경우로 생각하자.
그리고 top이 있는 경우와 없는 경우
1. top이 있는 경우
1-1. 이전 삼각형이 제일 오른쪽의 삼각형을 칠한 경우
1-1-1. 제일 오른쪽을 칠한 경우는 한가지.
1-1-2. 제일 오른쪽을 안칠한 경우는 두가지
1-2. 이전 삼각형이 제일 오른쪽의 삼각형을 칠하지 않은 경우
1-2-1. 제일 오른쪽을 칠한 경우는 그래도 한가지
1-2-2. 제일 오른쪽을 안칠한 경우는 세가지
2. top이 없는 경우
1-1. 이전 삼각형이 제일 오른쪽의 삼각형을 칠한 경우
1-1-1. 제일 오른쪽을 칠한 경우는 한가지.
1-1-2. 제일 오른쪽을 안칠한 경우는 한가지
1-2. 이전 삼각형이 제일 오른쪽의 삼각형을 칠하지 않은 경우
1-2-1. 제일 오른쪽을 칠한 경우는 그래도 한가지
1-2-2. 제일 오른쪽을 안칠한 경우는 두가지
이렇게 이어붙이면 되겠다.
"""
from dataclasses import dataclass

@dataclass
class Case:
    paint_count: int = 0
    unpaint_count: int = 0
    
    @property
    def total_count(self):
        return self.paint_count + self.unpaint_count
    
def append(i, cases, tops):
    prior_case = cases[i-1]
    case = cases[i]
    
    case.paint_count = prior_case.total_count % 10007
    case.unpaint_count = (prior_case.total_count * (1 + tops[i]) + prior_case.unpaint_count) % 10007

def solution(n, tops):
    cases = [Case() for _ in range(n)]
    cases[0].paint_count = 1
    cases[0].unpaint_count = 2 + tops[0]
    
    for i in range(1, n):
        append(i, cases, tops)
    
    return cases[-1].total_count % 10007