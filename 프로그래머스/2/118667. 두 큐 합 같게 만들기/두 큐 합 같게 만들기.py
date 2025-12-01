"""
그리디로 되나? -> 안될듯
q1 길이 q2 길이 모두 30만 -> 실제로 큐에 넣고 빼는건 안될듯
원소가 최대 10 ** 9 헉

합을 구해서 1/2. 왼쪽에서 빼고 오른쪽에는 더해서 하면 될거 같은데, 누적합..?

크면 더하고 작으면 빼도 될듯
"""

def solution(queue1, queue2):
    acc = [0] * (len(queue1) + len(queue2) + 1)
    for i, q in enumerate(queue1 + queue2, start=1):
        acc[i] = acc[i-1] + q
    
    if acc[-1] % 2:
        return -1
    
    target = acc[-1] // 2
    i = 0
    j = len(queue1)
    
    cnt = 0
    while i < j and j < len(acc):
        value = acc[j] - acc[i]
        if value == target:
            return cnt
        if value > target:
            i += 1
        else:
            j += 1
        cnt += 1
            
    return -1