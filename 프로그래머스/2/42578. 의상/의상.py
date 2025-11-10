def solution(clothes):
    d = dict()
    for name, cat in clothes:
        d[cat] = (d.get(cat) or 1) + 1
    cnt = 1
    for v in d.values():
        cnt *= v
    return cnt - 1