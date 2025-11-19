def solution(money):
    a, b, c, d = 0, money[0], money[1], 0
    
    for i, m in enumerate(money[2:], start=2):
        a, b, c, d = b + m, max(a, b), d + m, max(c, d)
    
    return max(b, c, d)