"""
brown부터 가자. brown 은 // 2를 해주고, -2를 해주면 이걸로 찾아가는거지.
"""
def solution(brown, yellow):
    w_h = brown // 2 - 2
    h = w_h // 2
    w = h + (1 if w_h % 2 else 0)
    
    while w * h != yellow:
        w += 1
        h -= 1
        
    return [w + 2, h + 2]