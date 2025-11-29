"""
두 번 이상 방문 가능. 오..

사전 순으로 가장 빠른 경로? -> dfs로 가되, 그 순서를 사전 순으로 넣으면 되려나.
d -> l -> r -> u
미로의 좌측 상단과 우측 하단은 1,1 3,4다. 일부러 패딩을 넣어주자

1. 탈출 가능한 경우
dfs로 최단 거리로 가다가 도착 지점에 이동 거리와 짝수 차이로 도착할 수 있을 때
2. 탈출 불가능한 경우
뭐.. 도착 못하거나 홀수 차례로만 도착할 수 있을 때

아니.. 미로에 못가는 길은 없나? 이게 맞나?

dfs보다 더 쉬울 것 같다.
k가 홀수고, 거리가 홀수면 갈 수 있다. k가 짝수고, 거리가 짝수면 갈 수 있다.
딱맞으면 그냥 순서대로 가면 되고.

우선은 최단 경로대로 짜놓고, 그다음에 추가할 수 있는거 추가하기.
어떻게 추가하지.

여유거리 // 2를 p를 계산해두고가자.
1. p와 바닥까지의 거리보다 작은 만큼 이동. 그만큼 u도 추가.
2. p와 left까지의 거리보다 작은 만큼 이동. 그만큼 r도 추가.
3. right - left 반복
4. up - down 반복
"""

def solution(n, m, x, y, r, c, k):
    d = abs(x-r) + abs(y-c)
    if d % 2 != k % 2 or d > k:
        return "impossible"
    routes = ["", "", "", ""]
    if x < r:
        routes[0] = 'd' * (r - x)
    else:
        routes[3] = 'u' * (x - r) or ''
    if y > c:
        routes[1] = 'l' * (y - c)
    else:
        routes[2] = 'r' * (c - y) or ''
    
    """
    d를 출발지 기준으로 더 붙이고(u도), l도 출발지 기준으로 더 붙이고(r도).
    이렇게 해도 남았다고 치자. 그러면?
    r 사이사이에 l 끼워넣고
    그래도 남는다면 u 사이에 d 끼워 넣고.
    그럼 이걸 어떻게 구현해야하지
    """
    
    p = (k - d) // 2
    
    d_space = n - max(x, r)
    if p >= d_space:
        p -= d_space
        routes[0] += 'd' * d_space
        routes[3] += 'u' * d_space
    else:
        routes[0] += 'd' * p
        routes[3] += 'u' * p
        return ''.join(routes)
    
    l_space = min(y, c) - 1
    if p >= l_space:
        p -= l_space
        routes[1] += 'l' * l_space
        routes[2] += 'r' * l_space
    else:
        routes[1] += 'l' * p
        routes[2] += 'r' * p
        return ''.join(routes)
    
    routes[2] = ('rl' * p or '') + routes[2]
    
    return ''.join(routes)