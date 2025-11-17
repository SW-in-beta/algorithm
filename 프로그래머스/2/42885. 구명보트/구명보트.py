"""
사람 수 50000이하.
무게는 40이상 240 이하
구명보트 제한 40이상 240 이하

큰 사람부터 넣고, 넣을 때는 큰 사람이 탄 곳 먼저 검토한다고 했을 때 틀릴 경우의 수?
몰라 없다치고 한 번 해보자.

큰 사람부터 들어간 곳을 어떻게 관리해야 효율적일까
항상 정렬된 상태를 유지하는 것?
아니면 매번 전부 비교하는 것?
비교 하는 것은 최대 n**2일 것 같은데
시간이 살짝 오바될 것 같다.
최대 heap? nlogn일거 같긴 하다. 한 번 해보기. 꺼냈다가 안맞으면 다시 넣기
맞으면 더해서 넣기
기본적으로 0인 보트도 하나 넣어놓자. X

두 번째 방법
정렬을 한 번 시키고
이분 탐색을 통해서 더할 대상을 찾아서 더하고 제거하기

heap 말고 bisect 활용하기.
아.. bisect는 역순으로 찾지 맞다...

아.. 최대 2명밖에 못타네... 하 왜케 작냐고
"""
def solution(people, limit):
    sorted_people = sorted(people, reverse=True)
    i = 0
    j = len(people) - 1
    while True:
        if i > j:
            break
        if i == j:
            i += 1
            break
        if sorted_people[i] + sorted_people[j] <= limit:
            j -= 1
        i += 1
    return i