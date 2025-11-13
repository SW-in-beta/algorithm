from heapq import heappush, heappop, heapify
def mix(a, b):
    return a + 2 * b
    
def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while len(scoville):
        s1 = heappop(scoville)
        if s1 >= K:
            break
        if len(scoville) == 0:
            return -1
        s2 = heappop(scoville)
        heappush(scoville, mix(s1, s2))
        answer += 1
    return answer