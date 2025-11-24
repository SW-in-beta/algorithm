"""
n개의 주사위, 각 주사위는 1~n.
A가 n / 2, B가 남은 것. 점수합산 후 더 큰쪽이 승리. -> n은 짝수일까?

주사위에는 1~6이 적혀있는 것이 아니다. 1~n까지
그리고 기댓값으로 붙는 것이 아니라, 실제 조합으로 결정.

n이 10이하. 원소는 100이하. 
6개의 수. 한명당 최대 6 ** 5만큼의 경우의 수가 생긴다.
두명이면 6 ** 10
그러면서 10개중에 5개 가져가는 케이스 10C5 -> 2*9*2*7
-> 시간 초과.

계산할 수 있는 경우가 있을 것 같다.
하나하나 비교하는게 아니고, 정렬을 한 뒤에 이진 탐색으로 들어가면 되지 않을까?
둘다 정렬을 시켜놓고, 하나하나 들어갈 자리를 찾는거지. bisect left와 bisect right 둘 다 써서
1. 주사위 인덱스가 주어졌을 때, 그 주사위 조합으로 가능한 모든 케이스 다 찾는다. -> sorted(Counter)로 반환
2. 서로 비교를 한다.
2-1. 작은거 순으로 비교하는데, 그 작은 수의 count와 개수를 다 곱해줘야한다.
2-2. 그리고 남은 큰거만큼 또 곱해주고, 그 다음은 큰 애들부터 비교
3. 그리고 모든 케이스를 비교해줄 필요는 없다. 한 번 계산하면 그 반대 케이스도 자동으로 계산 되는거니까.
"""
from itertools import product, combinations
from collections import Counter
from bisect import bisect_left as bl, bisect_right as br

def get_case(idxes, dice):
    return [sum(p) for p in product(*[dice[idx] for idx in idxes])]

def get_op_idxes(idxes):
    return tuple(i for i in range(len(idxes) * 2) if i not in idxes)

def fight(idxes, dice):
    op_idxes = get_op_idxes(idxes)
    case = Counter(get_case(idxes, dice))
    op_case = sorted(get_case(op_idxes, dice))
    total = 6 ** len(idxes)
    
    win = 0
    
    for key in sorted(case.keys()):
        l = bl(op_case, key)
        r = br(op_case, key)
        win += l * case[key]
        
    return win

def solution(dice):
    n = len(dice)
    records = dict()
    max_win = 0
    max_idxes = None
    for my_idxes in combinations(range(n), n // 2):
        win = fight(my_idxes, dice)
        if win > max_win:
            max_win = win
            max_idxes = my_idxes
                
    return [i+1 for i in sorted(max_idxes)]