"""
하나씩 입을수도 있고
두개씩 입을수도 있고
세개씩 입을수도 있고
n + 1개 가능한데, 모두가 0인 경우는 빼야지
"""
def solution(clothes):
    d = dict()
    for name, cat in clothes:
        d[cat] = (d.get(cat) or 1) + 1
    cnt = 1
    for v in d.values():
        cnt *= v
    return cnt - 1