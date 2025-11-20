"""
공항 수 3개 이상 10000개 이하
a -> b 방향 그래프

문제 정의
1. 항공권은 방향그래프
2. ICN에서 출발해서 다음 공항으로 이동. 결로가 2개 이상일 경우 작은게 먼저 -> 힙

모든 공항은 알파벳 대문자 3글자 -> 그냥 그대로 정렬하면 된다.
주어진 공항 수는 3개 이상 10,000개 이하 -> 시간 초과는 안뜬다.
a -> b 방향그래프.
주어진 항공권 모두 사용해야 합니다 -> 내가 중간에 나왔는데, 그게 문제인가. 근데 가는 길은 항상 있는데.

와 알았다.
가능한 경로가 2개 이상이라고 해서 무조건 알파벳 순서를 앞에 보내면 안된다.
앞 경로로 갔을 때 경로가 없을수도 있다..!

백트래킹이네 드디어
필요한 정보 : 거쳐간 경로? 이건 반복적으로 거쳐갈수도 있음. visited가 필요한게 아니다.
항공권과 현재 사용한 항공권..

하나밖에 없으면 그냥 써서 다음으로 넘기면 되고
만약 경로가 두개다.
그럼 하나 쓰고 넘기고, 만약 경로 수가 티켓 수랑 같으면 return
아니면 쓴거 취소하고 다른거 쓰고 다시 탐색 ㅇㅋ
"""
from collections import defaultdict

"""
코드 흐름을 정리해보자.
우선 종료조건부터.
더 방문할 곳으면 끝. 그게 도착했든 안했든

1. 출발지를 찾는다.
2. 출발지에서 갈 수 있는 항공권들을 본다.
3. 항공권을 썼다면 continue
4. 안썼으면 썼다고 치고, visited에도 추가하고 다음 dfs로 넘긴다.
5. 결과를 받았을 때 visited의 길이가 total이면 ㅇㅋ
6. 아니면 항공권 다시 안쓴거로 수정 + visited 원래 길이대로
"""
def dfs(visited, routes, total):
    dist = len(visited)
    dep = visited[-1]
    for ticket in routes[dep]:
        if ticket[1]:
            continue
        ticket[1] = True
        visited.append(ticket[0])
        visited = dfs(visited, routes, total)
        if len(visited) == total:
            break
        ticket[1] = False
        visited = visited[:dist]
    return visited

def solution(tickets):
    routes = defaultdict(list)
    for dep, arr in sorted(tickets, key=lambda x: x[1]):
        routes[dep].append([arr, False])
    total = len(tickets) + 1

    return dfs(['ICN'], routes, total)