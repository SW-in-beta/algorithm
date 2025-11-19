"""
순서는 바꿀 수 없다.
모든 경우의 수를 고려하기에는 숫자가 좀 많다.
2 ** 20이 되어야 할 것 같은데 -> 10 ** 7이니까 전부 탐색 가능
이걸 꼭 전부 탐색해야하나?
그 방법밖에 없을 것 같긴 하다. 중간에 예측을 할 수 없으니까.
deque나 stack이나 상관 없다.
"""
from collections import Counter

def solution(numbers, target):
    s = [0]
    for n in numbers:
        new_s = []
        while s:
            new_n = s.pop()
            new_s.append(new_n + n)
            new_s.append(new_n - n)
        s = new_s
        
    return Counter(s)[target]