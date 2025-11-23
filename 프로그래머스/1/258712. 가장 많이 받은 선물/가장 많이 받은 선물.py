"""
1.많이 준 사람이 받는다.
2.같으면? 선물 지수가 더 큰 사람이 작은 사람에게 받는다.
2-1. 선물 지수는 내가 준 선물 - 받은 선물
2-2. 선물 지수도 같다면 주고받지 않는다.

친구는 이름으로 관리 -> 들어온 순서대로 index 찾아줄까? -> 그냥 dictionary로 구현하자

이거 조합으로 풀면 모든 경우의 수를 구할 수 있다.
"""
from itertools import combinations
from collections import defaultdict
from dataclasses import dataclass, field

@dataclass
class Record:
    friend: str
    _record: dict = field(default_factory=lambda: defaultdict(int))
    
    @property
    def point(self):
        return sum(self._record.values())
    
    def point_to_friend(self, friend):
        return self._record[friend]
    
    def give(self, friend, count=1):
        self._record[friend] += count
        
    def take(self, friend, count=1):
        self._record[friend] -= count

def who_will_get_gift(a_record, b_record):
    if a_record.point_to_friend(b_record.friend) > 0:
        return a_record.friend
    elif a_record.point_to_friend(b_record.friend) < 0:
        return b_record.friend
    else:
        a_point = a_record.point
        b_point = b_record.point
        if a_point > b_point:
            return a_record.friend
        elif a_point < b_point:
            return b_record.friend
        
    return None
    
        
def solution(friends, gifts):
    records = {f: Record(f) for f in friends}
    
    for gift in gifts:
        sender, receiver = gift.split(' ')
        sender_record, receiver_record = records[sender], records[receiver]
        sender_record.give(receiver)
        receiver_record.take(sender)
        
    next_month_counts = {f: 0 for f in friends}
    for a, b in combinations(records.keys(), 2):
        a_record, b_record = records[a], records[b]
        target = who_will_get_gift(a_record, b_record)
        if target:
            next_month_counts[target] += 1
        
    return max(next_month_counts.values())