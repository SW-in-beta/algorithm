"""
모든 경우의 수를 다 비교하자

1. discount의 경우의 수를 모두 구한다.
2. 각 경우에서 이모티콘 플러스 서비스 가입자와 판매액을 구한다.
"""

from itertools import product
from dataclasses import dataclass

@dataclass
class Emoticon:
    price: int
    discount: int
    
    @property
    def discounted_price(self):
        return self.price * (100 - self.discount) // 100

def solution(users, emoticons):
    emoticon_cases = [[Emoticon(p, d) for p, d in zip(emoticons, discount)] for discount in product([10, 20, 30, 40], repeat=len(emoticons))]
    
    max_plus = 0
    max_total = 0
    for emoticon_case in emoticon_cases:
        plus = 0
        total = 0
        for discount, threshold in users:
            user_total = 0
            for emoticon in emoticon_case:
                if emoticon.discount < discount:
                    continue
                user_total += emoticon.discounted_price
            if user_total >= threshold:
                plus += 1
            else:
                total += user_total
        if max_plus < plus:
            max_plus = plus
            max_total = total
        elif max_plus == plus:
            max_total = max(max_total, total)
        
    return [max_plus, max_total]