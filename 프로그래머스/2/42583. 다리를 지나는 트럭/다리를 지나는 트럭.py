"""
정해진 순으로 건너야 한다.
길이와 무게 제한. length는 트럭의 개수 -> 이게 건너는 시간이다.
한대당 length만큼 건널 수 있다.
트럭이 끝날때까지 반복해보자.
"""
from collections import deque, namedtuple
Truck = namedtuple('Truck', ['time', 'weight'])

def solution(bridge_length, weight, truck_weights):
    t = 1
    truck_on_bridge = deque([])
    weight_on_bridge = 0
    for w in truck_weights:
        if truck_on_bridge and truck_on_bridge[0].time <= t:
            truck = truck_on_bridge.popleft()
            weight_on_bridge -= truck.weight
        if len(truck_on_bridge) >= bridge_length:
            truck = truck_on_bridge.popleft()
            t = truck.time
            weight_on_bridge -= truck.weight
        while weight_on_bridge + w > weight:
            truck = truck_on_bridge.popleft()
            t = truck.time
            weight_on_bridge -= truck.weight
        truck = Truck(t+bridge_length, w)
        truck_on_bridge.append(truck)
        weight_on_bridge += truck.weight
        print(t, truck_on_bridge)
        t += 1
    
    return truck_on_bridge[-1].time

bridge_length = 3
weight = 5
truck_weights = [2, 2, 2, 2, 2]