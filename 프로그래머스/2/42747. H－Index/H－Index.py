"""
h가 최소 인용 횟수이자 개수
"""

def solution(citations):
    h = 0
    for i, e in enumerate(sorted(citations)):
        num = len(citations) - i
        h = max(h, min(num, e))
    return h