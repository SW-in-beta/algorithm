"""
deliveries와 pickups가 남아있는 거 기준, 최대 거리부터 정렬해야할 듯 ->  정렬할 필요 없이 그냥 pop하면 된다.
왔다갔다 거리는 deliveries와 pickups의 거리중 최댓값

현재 논리
1. 배달할 박스나 수거할 박스가 있는 가장 먼 집부터 가야한다. 이건 무조건 갔다와야 하는 거리.
2. 어떻게 해도 한 번에 배달 또는 수거하는 개수가 cap개가 넘을 수 없다. -> 그러므로 그냥 한 번에 쭉 배달하고 오면서 수거
3. 그러니까 뒤에서부터 빼는거지

"""

def filtering(arr):
    while arr:
        if arr[-1] <= 0:
            arr.pop()
        else:
            break
            
def remove(cnt, arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= cnt:
            arr[i] -= cnt
            break
        cnt -= arr[i]
        arr[i] = 0

def solution(cap, n, deliveries, pickups):
    filtering(deliveries)
    filtering(pickups)
    
    total_dist = 0
    while deliveries or pickups:
        dist = max(len(deliveries), len(pickups))
        total_dist += dist * 2
        remove(cap, deliveries)
        remove(cap, pickups)
        filtering(deliveries)
        filtering(pickups)
        
    return total_dist