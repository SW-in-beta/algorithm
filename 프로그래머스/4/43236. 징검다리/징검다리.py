"""
제한 조건
distance 1 <= 10**9
n개를 제거해야 하는데, 최대 개수는 50,000개 이하

우선 바위를 정렬하고, 그 거리들을 정리하자.
2 9 3 3 4 4가 거리였는데, 제일 작은 2 제거(2, 9) 3 제거 (3, 3)
합이 가장 작은 순서대로 착착착 찾아서 제거하면 될 것 같은데

거리의 최솟값이 주어졌을 때, 몇개를 합쳐야 하는지 계산할 수 있나?
할 수 있을 것 같다. 자기 주변의 작은 값과 합치면 된다. 되는거 맞나?

min_dist보다 같거나 크면 그냥 넣는다. 커진다.
min_dist보다 작으면 이미 큐에 들어가 있는 마지막 애랑 내 다음 친구랑 비교해서 작은거랑 더한다. 만약 다음 친구를 더했으면 i는 +2로 커져야지.

구하고자 하는 것을 생각해보자.
n개 만큼 제거했을 때 구할 수 있는 거리의 최솟값의 최댓값
지금 내가 구한건 거리의 최솟값을 줬을때, n의 최솟값.
거리의 최솟값이 주어졌을 때 n은 여러개가 될 수 있겠지.

최솟값 중에 가장 큰 값을 찾는 것. 역시 l, r은 전체 범위
m으로 했을때 n보다 작거나 같다? l = m -> 작을때도 포함해야한다. 작다는 것은 도달할 수 있다는 의미
m으로 했을때 n보다 크다? r = m-1
"""
from collections import deque

def count(min_dist, rocks):
    cnt = 0
    prev = 0
    for r in rocks:
        if r - prev < min_dist:
            cnt += 1
            continue
        prev = r
    return cnt
        
def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    l = 0
    r = max(rocks)
    answer = 0
    while l <= r:
        m = (l + r) // 2
        cnt = count(m, rocks)
        if cnt <= n:
            answer = m
            l = m+1
        else:
            r = m-1
    
    return answer