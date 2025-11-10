"""
1. 장르 별로 가장 많이 재생된 노래 두 개 씩
2. 장르는 속한 노래가 가장 많이 재생된거 우선
3. 장르 -> 노래. 노래 재생 횟수 같으면 고유 번호 낮은 노래 순으로.
4. 고유번호는 인덱스

그렇게 어렵진 않다. 어떻게 해야 효율적일지가 문제

"""
from collections import defaultdict as dd

def solution(genres, plays):
    g_list = dd(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        g_list[g].append((p, -i))
    
    play_list = []
    for genre in sorted(set(genres), key=lambda g: sum(p for p, _ in g_list[g]), reverse=True):
        play_list.extend([-i for p, i in sorted(g_list[genre], reverse=True)][:2])
        
    return play_list